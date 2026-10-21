param([switch]$Uninstall)

$ErrorActionPreference = 'Stop'
$repoRoot = (Resolve-Path -LiteralPath (Join-Path $PSScriptRoot '..\..')).Path
if ($repoRoot -ne 'D:\exe\MaAiAudio') { throw "Unexpected repository path: $repoRoot" }

$python = Join-Path $env:LocalAppData 'Programs\Python\Python313\python.exe'
$runner = Join-Path $repoRoot 'automation\ai_short_video\runner.py'
if (-not (Test-Path -LiteralPath $python)) { throw "Python not found: $python" }
if (-not (Test-Path -LiteralPath $runner)) { throw "Runner not found: $runner" }

$definitions = @(
    @{ Name = 'MaAiAudio-AIVideo-Daily'; Mode = 'daily'; Trigger = New-ScheduledTaskTrigger -Daily -At '08:30' },
    @{ Name = 'MaAiAudio-AIVideo-Release'; Mode = 'release'; Trigger = New-ScheduledTaskTrigger -Daily -DaysInterval 3 -At '10:00' },
    @{ Name = 'MaAiAudio-AIVideo-Audit'; Mode = 'audit'; Trigger = New-ScheduledTaskTrigger -Weekly -DaysOfWeek Monday -At '11:00' }
)

foreach ($definition in $definitions) {
    if ($Uninstall) {
        Unregister-ScheduledTask -TaskName $definition.Name -Confirm:$false -ErrorAction SilentlyContinue
        continue
    }
    $action = New-ScheduledTaskAction -Execute $python -Argument "`"$runner`" $($definition.Mode)" -WorkingDirectory $repoRoot
    $settings = New-ScheduledTaskSettingsSet -StartWhenAvailable -MultipleInstances IgnoreNew -ExecutionTimeLimit (New-TimeSpan -Hours 4)
    Register-ScheduledTask -TaskName $definition.Name -Action $action -Trigger $definition.Trigger -Settings $settings -Description 'AI short-video research; creates review-only GitHub PRs.' -Force | Out-Null
}

if ($Uninstall) {
    Write-Output 'AI short-video schedules removed.'
} else {
    Get-ScheduledTask -TaskName 'MaAiAudio-AIVideo-*' | Select-Object TaskName, State
}

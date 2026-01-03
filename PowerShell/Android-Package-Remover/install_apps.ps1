param (
    [string]$l
)

# Check if file exists
if (-Not (Test-Path $l)) {
    Write-Host "File doesnt exist: $l"
    exit
}

$packages = Get-Content $l | Where-Object { $_ -notlike "#*" -and $_.Trim() -ne "" }

foreach ($package in $packages) {
    $command = "cmd package install-existing $package"
    .\adb.exe shell $command
}
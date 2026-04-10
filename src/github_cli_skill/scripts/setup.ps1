# GitHub CLI Skill Full Deployment Script
# Follows: docs/specs/skill_management_protocol.md

$SkillName = "github_cli_skill"
$GlobalSkillsDir = "C:\Users\kissi\.gemini\antigravity\skills"

# Get script parent directory
$ScriptDir = Split-Path -Parent $MyInvocation.MyCommand.Definition
$SourcePath = Resolve-Path (Join-Path $ScriptDir "..")

$TargetLink = Join-Path $GlobalSkillsDir $SkillName

Write-Host ">>> Starting Deployment: $SkillName" -ForegroundColor Cyan
Write-Host "Source: $SourcePath"
Write-Host "Target: $TargetLink"

try {
    if (Test-Path $TargetLink) {
        $ExistingItem = Get-Item $TargetLink
        if ($ExistingItem.Attributes -match "ReparsePoint") {
            Write-Warning "Global link already exists. To redeploy, please delete it manually: rm $TargetLink"
        } else {
            Write-Error "Error: Path '$TargetLink' exists and is not a link."
        }
    } else {
        # Create Symbolic Link
        New-Item -ItemType SymbolicLink -Path $TargetLink -Target $SourcePath.Path -ErrorAction Stop | Out-Null
        Write-Host "Success: Global Symbolic Link created." -ForegroundColor Green
    }
} catch {
    Write-Error "Deployment Failed: Please ensure you have Administrator privileges.`nError: $($_.Exception.Message)"
}

Write-Host ">>> Deployment Finished." -ForegroundColor Cyan

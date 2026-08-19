param(
    [string]$Path = "layouts/mp_marimo_2026_08_27.slides.json"
)

$ErrorActionPreference = "Stop"

if (-not (Test-Path -LiteralPath $Path)) {
    Write-Error "File not found: $Path"
    exit 1
}

$raw = Get-Content -LiteralPath $Path -Raw

try {
    $json = $raw | ConvertFrom-Json -AsHashtable -Depth 100
} catch {
    Write-Error "Invalid JSON in $Path`n$($_.Exception.Message)"
    exit 1
}

if (-not $json.ContainsKey("data") -or -not $json["data"].ContainsKey("cells")) {
    Write-Error "Expected 'data.cells' in $Path"
    exit 1
}

$cells = $json["data"]["cells"]
if (-not ($cells -is [System.Collections.IEnumerable])) {
    Write-Error "Expected 'data.cells' to be an array in $Path"
    exit 1
}

$missingNotes = @()
$nonStringNotes = @()
$cellCount = 0

foreach ($cell in $cells) {
    $cellCount += 1
    $index = $cellCount - 1

    if (-not ($cell -is [hashtable])) {
        $missingNotes += $index
        continue
    }

    if (-not $cell.ContainsKey("speakerNotes")) {
        $missingNotes += $index
        continue
    }

    $notes = $cell["speakerNotes"]
    if ($notes -isnot [string]) {
        $nonStringNotes += $index
        continue
    }

    if ([string]::IsNullOrWhiteSpace($notes)) {
        $missingNotes += $index
    }
}

if ($missingNotes.Count -gt 0 -or $nonStringNotes.Count -gt 0) {
    if ($missingNotes.Count -gt 0) {
        Write-Host ("Missing/empty speakerNotes at cell indexes: " + ($missingNotes -join ", ")) -ForegroundColor Yellow
    }
    if ($nonStringNotes.Count -gt 0) {
        Write-Host ("Non-string speakerNotes at cell indexes: " + ($nonStringNotes -join ", ")) -ForegroundColor Yellow
    }
    exit 1
}

Write-Host "OK: $Path" -ForegroundColor Green
Write-Host "Cells checked: $cellCount"
Write-Host "All cells contain non-empty string speakerNotes."
exit 0
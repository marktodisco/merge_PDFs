param ($envName, $filePath)

if ((-not [string]::IsNullOrEmpty("$envName")) -and (-not [string]::IsNullOrEmpty("$filePath"))) {
    conda env create -n "$envName" -f "$filePath"
    conda activate "$envName"
    pip install -e .
} else {
    Write-Error 'Both parameters "envName" and "filePath" must be specified.'
}

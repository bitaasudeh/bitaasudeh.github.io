# After creating a repository on GitHub, replace YOUR_USERNAME and YOUR_REPO_NAME below
# Then run this script: .\push-to-github.ps1

$repoUrl = "https://github.com/YOUR_USERNAME/YOUR_REPO_NAME.git"

# Add remote (if not already added)
git remote remove origin 2>$null
git remote add origin $repoUrl

# Push to GitHub
git branch -M main
git push -u origin main


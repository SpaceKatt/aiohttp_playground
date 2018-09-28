find ./docs -name "*.md" -type f -exec sh -c 'markdown "${0}" > "${0%.md}.html"' {} \; ; mv ./docs/*.html ./src/static/

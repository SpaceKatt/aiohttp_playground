find ./docs -name "*.md" \
     -type f \
     -exec sh -c 'pandoc -f markdown -t html5 -o "${0%.md}.html" "${0}"' {} \; \
     ; mv ./docs/*.html ./src/static/

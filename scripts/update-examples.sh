#!/bin/bash
# Update README example images
# Run this script when you make changes that affect the visual output

set -e

echo "🔄 Updating README example images..."

# Run the example generator
if ! python3 src/generate_examples.py; then
    echo "❌ Failed to generate examples"
    exit 1
fi

# Check if there are changes
if git diff --quiet docs/images/; then
    echo "✅ No changes to example images"
else
    echo "📝 Example images have been updated:"
    git diff --stat docs/images/
    echo ""
    echo "Please review the changes and commit them if they look correct:"
    echo "  git add docs/images/"
    echo "  git commit -m 'docs: update example images'"
fi
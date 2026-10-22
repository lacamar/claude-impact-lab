#!/usr/bin/env bash
set -euo pipefail
cd "$(dirname "${BASH_SOURCE[0]}")/.."

SPEC=$(echo packaging/*.spec)
NAME=$(basename "$SPEC" .spec)
VERSION=$(awk '/^Version:/ {print $2; exit}' "$SPEC")
SOURCE_DIR="$HOME/.local/rpm/sources/$NAME"
mkdir -p "$SOURCE_DIR" "$HOME/.local/rpm/specs"

ln -sf "$PWD/$SPEC" "$HOME/.local/rpm/specs/$NAME.spec"
git archive --prefix="$NAME-$VERSION/" -o "$SOURCE_DIR/$NAME-$VERSION.tar.gz" HEAD

mx-rpm --no-git-commit "$@" "$NAME"

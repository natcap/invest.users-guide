import os
from docutils.parsers.rst.directives import register_directive
from sphinx.directives.code import Highlight
from sphinx.directives.other import Only
from sphinx.directives.patches import MathDirective
import restructuredtext_lint

# Load our new directive
register_directive('only', Only)
register_directive('math', MathDirective)

# Lint our README
for path in os.listdir('./source/'):
    if path.endswith('.rst'):
        print(path)
        errors = restructuredtext_lint.lint_file(os.path.join('./source', path))
        for error in errors:
            print(error[0])
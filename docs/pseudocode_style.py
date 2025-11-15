from pygments.style import Style
from pygments.token import Keyword, Name, String, Number, Comment, Operator, Punctuation

class PseudocodeStyle(Style):
    default_style = ""
    styles = {
        # Keywords like def, class, if, else
        Keyword: '#0000FF',          # Blue

        # Constants like True, False, None
        Keyword.Constant: '#008000',      # Green

        # Identifiers
        Name: '#000000',                  # Black

        # Strings
        String: '#BA2121',                # Dark red

        # Numbers
        Number: '#008080',                # Teal

        # Comments
        Comment: 'italic #408080',        # Gray italic

        # Operators
        Operator: 'bold #000000',         # Black bold

        # Punctuation
        Punctuation: '#000000',           # Black
    }

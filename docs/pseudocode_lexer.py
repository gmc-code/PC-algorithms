from pygments.lexer import RegexLexer
from pygments.token import Keyword, Name, Operator, String, Number, Text, Punctuation

class PseudocodeLexer(RegexLexer):
    name = 'Pseudocode'
    aliases = ['pseudocode']
    filenames = []

    tokens = {
        'root': [
            # Keywords
            (r'\b(MAIN PROGRAM|FUNCTION|ENDFUNCTION|END\s+FUNCTION|PROCEDURE|ENDPROCEDURE|END\s+PROCEDURE|CALL|RETURN|IF|THEN|ELSEIF|ELSE|ENDIF|CASE|OF|ENDCASE|FOR|TO|STEP|ENDFOR|WHILE|ENDWHILE|REPEAT|UNTIL|DO|INPUT|OUTPUT|PRINT|READ|WRITE|AND|OR|NOT|TRUE|FALSE|ARRAY|LIST|RECORD|DECLARE|SET|BEGIN|START|END|EXIT|BREAK|CONTINUE|IS|IS IN|)\b', Keyword),

            # Identifiers
            (r'[A-Z]*', Name),

        ],
    }


from pygments.lexer import RegexLexer
from pygments.token import Keyword, Name, Operator, String, Number, Text, Punctuation

class PseudocodeLexer(RegexLexer):
    name = 'Pseudocode'
    aliases = ['pseudocode']
    filenames = []

    tokens = {
        'root': [
            # Keywords
            (r'\b(FUNCTION|ENDFUNCTION|END\s+FUNCTION|PROCEDURE|ENDPROCEDURE|END\s+PROCEDURE|CALL|RETURN|IF|THEN|ELSEIF|ELSE|ENDIF|CASE|OF|ENDCASE|FOR|TO|STEP|ENDFOR|WHILE|ENDWHILE|REPEAT|UNTIL|DO|INPUT|OUTPUT|PRINT|READ|WRITE|AND|OR|NOT|TRUE|FALSE|ARRAY|LIST|RECORD|DECLARE|SET|BEGIN|START|END|EXIT|BREAK|CONTINUE)\b', Keyword),

            # Identifiers
            (r'\b[A-Za-z_][A-Za-z0-9_]*\b', Name),

            # Strings (double-quoted or single-quoted)
            (r'".*?"', String),
            (r"'.*?'", String),

            # Numbers
            (r'\d+', Number),

            # Operators (include assignment arrow ←)
            (r'[/≠=<>%+\-*/←]', Operator),

            (r"[ \[\] \(\)\{\},;:.?!'\"]", Punctuation)
        ],
    }


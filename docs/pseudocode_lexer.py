from pygments.lexer import RegexLexer
from pygments.token import Keyword, Name, Operator, String, Number, Text

class PseudocodeLexer(RegexLexer):
    name = 'Pseudocode'
    aliases = ['pseudocode']
    filenames = []

    tokens = {
        'root': [
            (r'\b(FUNCTION|END FUNCTION|PROCEDURE|END PROCEDURE|CALL|RETURN|IF|THEN|ELSEIF|ELSE|ENDIF|CASE|OF|ENDCASE|FOR|TO|STEP|ENDFOR|WHILE|ENDWHILE|REPEAT|UNTIL|DO|INPUT|OUTPUT|PRINT|READ|WRITE|AND|OR|NOT|TRUE|FALSE|ARRAY|LIST|RECORD|DECLARE|SET|BEGIN|START|END|EXIT|BREAK|CONTINUE)\b', Keyword),
            (r'\b[A-Za-z_][A-Za-z0-9_]*\b', Name),
            (r'".*?"', String),
            (r'\d+', Number),
            (r'[=<>%+\-*/]', Operator),
            (r'\s+', Text),
        ]
    }

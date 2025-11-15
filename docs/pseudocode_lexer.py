# from pygments.lexer import RegexLexer
# from pygments.token import Keyword, Name, Operator, String, Number, Text

# class PseudocodeLexer(RegexLexer):
#     name = 'Pseudocode'
#     aliases = ['pseudocode']
#     filenames = []

#     tokens = {
#         'root': [
#             (r'\b(FUNCTION|ENDFUNCTION|END FUNCTION|PROCEDURE|ENDPROCEDURE|END PROCEDURE|CALL|RETURN|IF|THEN|ELSEIF|ELSE|ENDIF|CASE|OF|ENDCASE|FOR|TO|STEP|ENDFOR|WHILE|ENDWHILE|REPEAT|UNTIL|DO|INPUT|OUTPUT|PRINT|READ|WRITE|AND|OR|NOT|TRUE|FALSE|ARRAY|LIST|RECORD|DECLARE|SET|BEGIN|START|END|EXIT|BREAK|CONTINUE)\b', Keyword),
#             (r'\b[A-Za-z_][A-Za-z0-9_]*\b', Name),
#             (r'".*?"', String),
#             (r'\d+', Number),
#             (r'[=<>%+\-*/]', Operator),
#             (r'\s+', Text),
#         ]
#     }
from pygments.lexer import RegexLexer
from pygments.token import Keyword, Name, Operator, String, Number, Text, Punctuation

class PseudocodeLexer(RegexLexer):
    name = 'Pseudocode'
    aliases = ['pseudocode']
    filenames = []

    tokens = {
        'root': [
            # Keywords
            (r'\b(FUNCTION|ENDFUNCTION|END FUNCTION|PROCEDURE|ENDPROCEDURE|END PROCEDURE|CALL|RETURN|IF|THEN|ELSEIF|ELSE|ENDIF|CASE|OF|ENDCASE|FOR|TO|STEP|ENDFOR|WHILE|ENDWHILE|REPEAT|UNTIL|DO|INPUT|OUTPUT|PRINT|READ|WRITE|AND|OR|NOT|TRUE|FALSE|ARRAY|LIST|RECORD|DECLARE|SET|BEGIN|START|END|EXIT|BREAK|CONTINUE)\b', Keyword),

            # Identifiers
            (r'\b[A-Za-z_][A-Za-z0-9_]*\b', Name),

            # Strings
            (r'".*?"', String),

            # Numbers
            (r'\d+', Number),

            # Operators
            (r'[=<>%+\-*/]', Operator),

            # Brackets and commas as punctuation
           (r'[\[\]\(\)\{\},;:.?!\'"]', Punctuation),

    }

from pygments.lexer import RegexLexer
from pygments.token import Keyword, Name, Text
class VcaaPseudocodeLexer(RegexLexer):
    name = 'VcaaPseudocode'
    aliases = ['vcaapseudocode']
    filenames = []

    tokens = {
        'root': [
            # Keywords
            (r'\b(MAIN PROGRAM|DEFINE|FUNCTION|ENDFUNCTION|END\s+FUNCTION|PROCEDURE|ENDPROCEDURE|END\s+PROCEDURE|PROCESS|END\s+PROCESS|CALL|RETURN|IF|THEN|ELSEIF|ELSE\s+IF|ELSE|ENDIF|END\s+IF|CASE|OF|ENDCASE|END\s+CASE|FOR|TO|STEP|ENDFOR|END\s+FOR|WHILE|ENDWHILE|END\s+WHILE|LOOP|REPEAT|UNTIL|END\s+UNTIL|DO|EXIT\s+WHEN|INPUT|OUTPUT|PRINT|READ|WRITE|DISPLAY|SHOW|PROMPT|SCAN|WRITE\s+LINE|READ\s+LINE|AND|OR|NOT|TRUE|FALSE|ARRAY|LIST|RECORD|TABLE|STACK|QUEUE|DECLARE|CONSTANT|VARIABLE|TYPE|OF\s+TYPE|SET|SET\s+OF|BEGIN|START|END|EXIT|BREAK|CONTINUE|COMMENT|WITH|BY|DEFAULT|OTHERWISE|NULL|EMPTY|IS|IN)\b', Keyword),


            # Any other ALL CAPS identifiers of atleast 2 letters
            (r'\b[A-Z]{2,}[A-Z_]*\b', Name),

            # Default: everything else
            (r'.', Text),

        ],
    }


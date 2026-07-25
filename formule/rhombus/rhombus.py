import base64
import zlib

dot_code = """digraph "Ромб" {
    rankdir=TB;
    node[fontname="Times-Roman" fontsize=14 style=filled penwidth=2.5];
    edge[penwidth=2.5 arrowsize=1.2];

    node[shape=ellipse fillcolor="#E3F2FD" color="#1E88E5"];
    a [label=<<I>a</I>>, tooltip="Страница"];
    h [label=<<I>h</I>>, tooltip="Висина"];
    d1[label=<<I>d</I><SUB><FONT POINT-SIZE="10">1</FONT></SUB>>, tooltip="Једна дијагонала"];
    d2[label=<<I>d</I><SUB><FONT POINT-SIZE="10">2</FONT></SUB>>, tooltip="Друга дијагонала"];
    P [label=<<I>P</I>>, tooltip="Површина"];
    ru[label=<<I>r</I><SUB><FONT POINT-SIZE="10"><I>u</I></FONT></SUB>>, tooltip="Полупречник уписане кружнице"];

    node[shape=box style="filled, rounded" fillcolor="#FFFDE7" color="#FBC02D"];
    
    // Формула: P = a * h
    P0 [label=<<I>P</I> = <I>a</I> · <I>h</I>>, tooltip="Површина као код паралелограма"];
    
    // Формула са разломком: P = (d1 * d2) / 2
    P1 [label=<
        <TABLE BORDER="0" CELLBORDER="0" CELLSPACING="0" CELLPADDING="0">
            <TR>
                <TD VALIGN="MIDDLE"><I>P</I> = &nbsp;</TD>
                <TD>
                    <TABLE BORDER="0" CELLBORDER="0" CELLSPACING="0" CELLPADDING="1">
                        <TR><TD ALIGN="CENTER"><I>d</I><SUB><FONT POINT-SIZE="10">1</FONT></SUB> · <I>d</I><SUB><FONT POINT-SIZE="10">2</FONT></SUB></TD></TR>
                        <HR/>
                        <TR><TD ALIGN="CENTER">2</TD></TR>
                    </TABLE>
                </TD>
            </TR>
        </TABLE>
    >, tooltip="Површина као код делтоида"];
    
    // Формула са разломком и степенима: a^2 = (d1^2 + d2^2) / 4
    a2 [label=<
        <TABLE BORDER="0" CELLBORDER="0" CELLSPACING="0" CELLPADDING="0">
            <TR>
                <TD VALIGN="MIDDLE"><I>a</I><SUP><FONT POINT-SIZE="10">2</FONT></SUP> = &nbsp;</TD>
                <TD>
                    <TABLE BORDER="0" CELLBORDER="0" CELLSPACING="0" CELLPADDING="1">
                        <TR><TD ALIGN="CENTER"><I>d</I><SUB><FONT POINT-SIZE="10">1</FONT></SUB><SUP><FONT POINT-SIZE="10">2</FONT></SUP> + <I>d</I><SUB><FONT POINT-SIZE="10">2</FONT></SUB><SUP><FONT POINT-SIZE="10">2</FONT></SUP></TD></TR>
                        <HR/>
                        <TR><TD ALIGN="CENTER">4</TD></TR>
                    </TABLE>
                </TD>
            </TR>
        </TABLE>
    >, tooltip="Примена Питагорине теореме"];
    
    // Формула: h = 2 * ru
    r0 [label=<<I>h</I> = 2<I>r</I><SUB><FONT POINT-SIZE="10"><I>u</I></FONT></SUB>>, tooltip="Висина је пречник"];

    a, h -> P0 -> P;
    d1, d2 -> P1 -> P;
    d1, d2 -> a2 -> a;
    ru -> r0 -> h;
}"""

# Kroki uses deflate compression, then urlsafe base64
compressed = zlib.compress(dot_code.encode('utf-8'), 9)
encoded = base64.urlsafe_b64encode(compressed).decode('utf-8')
print("Encoded length:", len(encoded))
print("https://kroki.io/graphviz/svg/" + encoded)

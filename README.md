# Proyecto Python

## Descripción

El presente programa es un juego de gato con interfaz gráfica de tkinter, asimismo se apoya en un juego de gato realizado enteramente con matrices, lo cual permite el entendimiento principal del juego. Ahora bien, el programa que contiene la interfaz gráfica se apoya del juego con matrices para aplicar la lógica que este conlleva. Para poder producir la interfaz gráfica se emplea tkinter, este nos provee un tablero, en cual se ejecuta el juego. Además, con el uso de este módulo se realiza un mensaje Pop Up donde se indica que la persona puede reiniciar el juego o no. 


### Metodología del juego
El juego consiste en un tablero de gato, un jugador debe escoger ser 'X' y el otro 'O'. El primer jugador debe escoger debe escoger una casilla para colocar su movimiento, de esta forma el otro jugador realiza lo mismo, y estos se turnan hasta terminar la partida. La partida termina cuando uno de los jugadores logra formar tres de sus símbolos en línea. Si el juego, no determina un ganador, el juego queda en empate. 

### Diagrama de flujo
[Uploading ticTacToe.d<mxfile host="app.diagrams.net" modified="2023-12-05T21:11:37.680Z" agent="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36" etag="SHnF9slW-MPi0wOjgexQ" version="22.1.5" type="google">
  <diagram id="C5RBs43oDa-KdzZeNtuy" name="Page-1">
    <mxGraphModel grid="1" page="1" gridSize="10" guides="1" tooltips="1" connect="1" arrows="1" fold="1" pageScale="1" pageWidth="827" pageHeight="1169" math="0" shadow="0">
      <root>
        <mxCell id="WIyWlLk6GJQsqaUBKTNV-0" />
        <mxCell id="WIyWlLk6GJQsqaUBKTNV-1" parent="WIyWlLk6GJQsqaUBKTNV-0" />
        <mxCell id="WIyWlLk6GJQsqaUBKTNV-2" value="" style="rounded=0;html=1;jettySize=auto;orthogonalLoop=1;fontSize=11;endArrow=block;endFill=0;endSize=8;strokeWidth=1;shadow=0;labelBackgroundColor=none;edgeStyle=orthogonalEdgeStyle;" edge="1" parent="WIyWlLk6GJQsqaUBKTNV-1" target="WIyWlLk6GJQsqaUBKTNV-6">
          <mxGeometry relative="1" as="geometry">
            <mxPoint x="360" y="120" as="sourcePoint" />
          </mxGeometry>
        </mxCell>
        <mxCell id="WIyWlLk6GJQsqaUBKTNV-6" value="Decides which &lt;br&gt;player goes first" style="rhombus;whiteSpace=wrap;html=1;shadow=0;fontFamily=Helvetica;fontSize=12;align=center;strokeWidth=1;spacing=6;spacingTop=-4;fillColor=#e1d5e7;strokeColor=#9673a6;" vertex="1" parent="WIyWlLk6GJQsqaUBKTNV-1">
          <mxGeometry x="280" y="160" width="160" height="90" as="geometry" />
        </mxCell>
        <mxCell id="zi1npzBdflfuzsiFVQyd-0" value="" style="ellipse;whiteSpace=wrap;html=1;fillColor=#dae8fc;strokeColor=#6c8ebf;" vertex="1" parent="WIyWlLk6GJQsqaUBKTNV-1">
          <mxGeometry x="300" y="40" width="120" height="80" as="geometry" />
        </mxCell>
        <mxCell id="zi1npzBdflfuzsiFVQyd-2" value="&lt;div style=&quot;&quot;&gt;&lt;span style=&quot;background-color: initial;&quot;&gt;&lt;br&gt;&lt;/span&gt;&lt;/div&gt;&lt;div style=&quot;&quot;&gt;&lt;span style=&quot;background-color: initial;&quot;&gt;Start Game&lt;/span&gt;&lt;/div&gt;" style="text;whiteSpace=wrap;html=1;align=center;" vertex="1" parent="WIyWlLk6GJQsqaUBKTNV-1">
          <mxGeometry x="310" y="55" width="100" height="50" as="geometry" />
        </mxCell>
        <mxCell id="zi1npzBdflfuzsiFVQyd-4" value="" style="whiteSpace=wrap;html=1;aspect=fixed;" vertex="1" parent="WIyWlLk6GJQsqaUBKTNV-1">
          <mxGeometry x="320" y="290" width="80" height="80" as="geometry" />
        </mxCell>
        <mxCell id="zi1npzBdflfuzsiFVQyd-5" value="&lt;div style=&quot;text-align: center;&quot;&gt;&lt;div style=&quot;border-color: var(--border-color);&quot;&gt;Takes turns between players.&lt;/div&gt;&lt;div style=&quot;border-color: var(--border-color);&quot;&gt;&lt;span style=&quot;border-color: var(--border-color); background-color: initial;&quot;&gt;Player 1 is X.&lt;/span&gt;&lt;/div&gt;&lt;div style=&quot;border-color: var(--border-color);&quot;&gt;&lt;span style=&quot;border-color: var(--border-color); background-color: initial;&quot;&gt;Player 2 is O.&lt;/span&gt;&lt;/div&gt;&lt;/div&gt;" style="text;whiteSpace=wrap;html=1;fillColor=#f8cecc;strokeColor=#b85450;" vertex="1" parent="WIyWlLk6GJQsqaUBKTNV-1">
          <mxGeometry x="320" y="290" width="80" height="80" as="geometry" />
        </mxCell>
        <mxCell id="zi1npzBdflfuzsiFVQyd-6" value="" style="whiteSpace=wrap;html=1;aspect=fixed;" vertex="1" parent="WIyWlLk6GJQsqaUBKTNV-1">
          <mxGeometry x="310" y="430" width="100" height="100" as="geometry" />
        </mxCell>
        <mxCell id="zi1npzBdflfuzsiFVQyd-8" value="" style="endArrow=classic;html=1;rounded=0;entryX=0.5;entryY=0;entryDx=0;entryDy=0;exitX=0.5;exitY=1;exitDx=0;exitDy=0;" edge="1" parent="WIyWlLk6GJQsqaUBKTNV-1" source="zi1npzBdflfuzsiFVQyd-5" target="zi1npzBdflfuzsiFVQyd-6">
          <mxGeometry width="50" height="50" relative="1" as="geometry">
            <mxPoint x="680" y="320" as="sourcePoint" />
            <mxPoint x="730" y="270" as="targetPoint" />
          </mxGeometry>
        </mxCell>
        <mxCell id="zi1npzBdflfuzsiFVQyd-9" value="" style="endArrow=classic;html=1;rounded=0;entryX=0.5;entryY=0;entryDx=0;entryDy=0;exitX=0.5;exitY=1;exitDx=0;exitDy=0;" edge="1" parent="WIyWlLk6GJQsqaUBKTNV-1" source="WIyWlLk6GJQsqaUBKTNV-6" target="zi1npzBdflfuzsiFVQyd-5">
          <mxGeometry width="50" height="50" relative="1" as="geometry">
            <mxPoint x="370" y="380" as="sourcePoint" />
            <mxPoint x="370" y="440" as="targetPoint" />
          </mxGeometry>
        </mxCell>
        <mxCell id="zi1npzBdflfuzsiFVQyd-10" value="Result is determined &lt;br&gt;after a combination&lt;br&gt;&amp;nbsp;of three is done." style="text;whiteSpace=wrap;html=1;align=center;fillColor=#f8cecc;strokeColor=#b85450;" vertex="1" parent="WIyWlLk6GJQsqaUBKTNV-1">
          <mxGeometry x="310" y="430" width="100" height="100" as="geometry" />
        </mxCell>
        <mxCell id="zi1npzBdflfuzsiFVQyd-13" value="" style="whiteSpace=wrap;html=1;aspect=fixed;fillColor=#d5e8d4;strokeColor=#82b366;" vertex="1" parent="WIyWlLk6GJQsqaUBKTNV-1">
          <mxGeometry x="327.5" y="585" width="65" height="65" as="geometry" />
        </mxCell>
        <mxCell id="zi1npzBdflfuzsiFVQyd-14" value="&lt;br&gt;Tie" style="text;whiteSpace=wrap;html=1;align=center;" vertex="1" parent="WIyWlLk6GJQsqaUBKTNV-1">
          <mxGeometry x="335" y="590" width="50" height="40" as="geometry" />
        </mxCell>
        <mxCell id="zi1npzBdflfuzsiFVQyd-21" value="" style="whiteSpace=wrap;html=1;aspect=fixed;" vertex="1" parent="WIyWlLk6GJQsqaUBKTNV-1">
          <mxGeometry x="440" y="585" width="65" height="65" as="geometry" />
        </mxCell>
        <mxCell id="zi1npzBdflfuzsiFVQyd-22" value="Player&lt;br&gt;&amp;nbsp;2&amp;nbsp;&lt;br&gt;wins" style="text;whiteSpace=wrap;html=1;align=center;fillColor=#d5e8d4;strokeColor=#82b366;" vertex="1" parent="WIyWlLk6GJQsqaUBKTNV-1">
          <mxGeometry x="440" y="585" width="62.5" height="65" as="geometry" />
        </mxCell>
        <mxCell id="zi1npzBdflfuzsiFVQyd-24" value="" style="whiteSpace=wrap;html=1;aspect=fixed;" vertex="1" parent="WIyWlLk6GJQsqaUBKTNV-1">
          <mxGeometry x="210" y="585" width="65" height="65" as="geometry" />
        </mxCell>
        <mxCell id="zi1npzBdflfuzsiFVQyd-25" value="Player&lt;br&gt;1&lt;br&gt;wins" style="text;whiteSpace=wrap;html=1;align=center;fillColor=#d5e8d4;strokeColor=#82b366;" vertex="1" parent="WIyWlLk6GJQsqaUBKTNV-1">
          <mxGeometry x="210" y="585" width="62.5" height="65" as="geometry" />
        </mxCell>
        <mxCell id="zi1npzBdflfuzsiFVQyd-26" value="" style="endArrow=classic;html=1;rounded=0;entryX=0.5;entryY=0;entryDx=0;entryDy=0;exitX=1;exitY=0.5;exitDx=0;exitDy=0;" edge="1" parent="WIyWlLk6GJQsqaUBKTNV-1" source="zi1npzBdflfuzsiFVQyd-10" target="zi1npzBdflfuzsiFVQyd-22">
          <mxGeometry width="50" height="50" relative="1" as="geometry">
            <mxPoint x="370" y="540" as="sourcePoint" />
            <mxPoint x="370" y="595" as="targetPoint" />
            <Array as="points">
              <mxPoint x="471" y="480" />
            </Array>
          </mxGeometry>
        </mxCell>
        <mxCell id="zi1npzBdflfuzsiFVQyd-27" value="" style="endArrow=classic;html=1;rounded=0;exitX=0;exitY=0.5;exitDx=0;exitDy=0;entryX=0.5;entryY=0;entryDx=0;entryDy=0;" edge="1" parent="WIyWlLk6GJQsqaUBKTNV-1" source="zi1npzBdflfuzsiFVQyd-10" target="zi1npzBdflfuzsiFVQyd-25">
          <mxGeometry width="50" height="50" relative="1" as="geometry">
            <mxPoint x="460" y="570" as="sourcePoint" />
            <mxPoint x="510" y="520" as="targetPoint" />
            <Array as="points">
              <mxPoint x="241" y="480" />
            </Array>
          </mxGeometry>
        </mxCell>
        <mxCell id="zi1npzBdflfuzsiFVQyd-28" value="Finish the &lt;br&gt;game or &lt;br&gt;restart" style="rhombus;whiteSpace=wrap;html=1;shadow=0;fontFamily=Helvetica;fontSize=12;align=center;strokeWidth=1;spacing=6;spacingTop=-4;fillColor=#e1d5e7;strokeColor=#9673a6;" vertex="1" parent="WIyWlLk6GJQsqaUBKTNV-1">
          <mxGeometry x="278.75" y="710" width="160" height="90" as="geometry" />
        </mxCell>
        <mxCell id="zi1npzBdflfuzsiFVQyd-34" value="" style="endArrow=classic;html=1;rounded=0;exitX=0.5;exitY=1;exitDx=0;exitDy=0;entryX=0.5;entryY=0;entryDx=0;entryDy=0;" edge="1" parent="WIyWlLk6GJQsqaUBKTNV-1" source="zi1npzBdflfuzsiFVQyd-10" target="zi1npzBdflfuzsiFVQyd-13">
          <mxGeometry width="50" height="50" relative="1" as="geometry">
            <mxPoint x="390" y="610" as="sourcePoint" />
            <mxPoint x="370" y="570" as="targetPoint" />
          </mxGeometry>
        </mxCell>
        <mxCell id="zi1npzBdflfuzsiFVQyd-35" value="" style="endArrow=classic;html=1;rounded=0;exitX=0.5;exitY=1;exitDx=0;exitDy=0;" edge="1" parent="WIyWlLk6GJQsqaUBKTNV-1" source="zi1npzBdflfuzsiFVQyd-13" target="zi1npzBdflfuzsiFVQyd-28">
          <mxGeometry width="50" height="50" relative="1" as="geometry">
            <mxPoint x="410" y="750" as="sourcePoint" />
            <mxPoint x="460" y="700" as="targetPoint" />
          </mxGeometry>
        </mxCell>
        <mxCell id="zi1npzBdflfuzsiFVQyd-36" value="" style="endArrow=classic;html=1;rounded=0;exitX=0.5;exitY=1;exitDx=0;exitDy=0;entryX=1;entryY=0.5;entryDx=0;entryDy=0;" edge="1" parent="WIyWlLk6GJQsqaUBKTNV-1" source="zi1npzBdflfuzsiFVQyd-22" target="zi1npzBdflfuzsiFVQyd-28">
          <mxGeometry width="50" height="50" relative="1" as="geometry">
            <mxPoint x="470" y="680" as="sourcePoint" />
            <mxPoint x="460" y="700" as="targetPoint" />
            <Array as="points">
              <mxPoint x="450" y="755" />
            </Array>
          </mxGeometry>
        </mxCell>
        <mxCell id="zi1npzBdflfuzsiFVQyd-37" value="" style="endArrow=classic;html=1;rounded=0;exitX=0.5;exitY=1;exitDx=0;exitDy=0;entryX=0;entryY=0.5;entryDx=0;entryDy=0;" edge="1" parent="WIyWlLk6GJQsqaUBKTNV-1" source="zi1npzBdflfuzsiFVQyd-25" target="zi1npzBdflfuzsiFVQyd-28">
          <mxGeometry width="50" height="50" relative="1" as="geometry">
            <mxPoint x="410" y="720" as="sourcePoint" />
            <mxPoint x="460" y="670" as="targetPoint" />
            <Array as="points">
              <mxPoint x="260" y="750" />
              <mxPoint x="270" y="750" />
            </Array>
          </mxGeometry>
        </mxCell>
        <mxCell id="zi1npzBdflfuzsiFVQyd-39" value="" style="ellipse;whiteSpace=wrap;html=1;fillColor=#dae8fc;strokeColor=#6c8ebf;" vertex="1" parent="WIyWlLk6GJQsqaUBKTNV-1">
          <mxGeometry x="300" y="860" width="120" height="80" as="geometry" />
        </mxCell>
        <mxCell id="zi1npzBdflfuzsiFVQyd-40" value="&lt;div style=&quot;&quot;&gt;&lt;br&gt;&lt;/div&gt;&lt;div style=&quot;&quot;&gt;End&lt;/div&gt;" style="text;whiteSpace=wrap;html=1;align=center;" vertex="1" parent="WIyWlLk6GJQsqaUBKTNV-1">
          <mxGeometry x="310" y="875" width="100" height="50" as="geometry" />
        </mxCell>
        <mxCell id="zi1npzBdflfuzsiFVQyd-42" value="" style="endArrow=classic;html=1;rounded=0;exitX=0.5;exitY=1;exitDx=0;exitDy=0;entryX=0.5;entryY=0;entryDx=0;entryDy=0;" edge="1" parent="WIyWlLk6GJQsqaUBKTNV-1" source="zi1npzBdflfuzsiFVQyd-28" target="zi1npzBdflfuzsiFVQyd-39">
          <mxGeometry width="50" height="50" relative="1" as="geometry">
            <mxPoint x="190" y="770" as="sourcePoint" />
            <mxPoint x="160" y="880" as="targetPoint" />
          </mxGeometry>
        </mxCell>
        <mxCell id="zi1npzBdflfuzsiFVQyd-43" value="" style="whiteSpace=wrap;html=1;aspect=fixed;fillColor=#fff2cc;strokeColor=#d6b656;" vertex="1" parent="WIyWlLk6GJQsqaUBKTNV-1">
          <mxGeometry x="610" y="715" width="80" height="80" as="geometry" />
        </mxCell>
        <mxCell id="zi1npzBdflfuzsiFVQyd-44" value="New game" style="text;html=1;strokeColor=none;fillColor=none;align=center;verticalAlign=middle;whiteSpace=wrap;rounded=0;" vertex="1" parent="WIyWlLk6GJQsqaUBKTNV-1">
          <mxGeometry x="620" y="740" width="60" height="30" as="geometry" />
        </mxCell>
        <mxCell id="zi1npzBdflfuzsiFVQyd-45" value="" style="endArrow=classic;html=1;rounded=0;entryX=0;entryY=0.5;entryDx=0;entryDy=0;exitX=1;exitY=0.5;exitDx=0;exitDy=0;" edge="1" parent="WIyWlLk6GJQsqaUBKTNV-1" source="zi1npzBdflfuzsiFVQyd-28" target="zi1npzBdflfuzsiFVQyd-43">
          <mxGeometry width="50" height="50" relative="1" as="geometry">
            <mxPoint x="190" y="580" as="sourcePoint" />
            <mxPoint x="240" y="530" as="targetPoint" />
          </mxGeometry>
        </mxCell>
        <mxCell id="zi1npzBdflfuzsiFVQyd-46" value="" style="endArrow=classic;html=1;rounded=0;exitX=0.5;exitY=0;exitDx=0;exitDy=0;entryX=1;entryY=0.5;entryDx=0;entryDy=0;" edge="1" parent="WIyWlLk6GJQsqaUBKTNV-1" source="zi1npzBdflfuzsiFVQyd-43" target="zi1npzBdflfuzsiFVQyd-0">
          <mxGeometry width="50" height="50" relative="1" as="geometry">
            <mxPoint x="10" y="580" as="sourcePoint" />
            <mxPoint x="60" y="530" as="targetPoint" />
            <Array as="points">
              <mxPoint x="650" y="80" />
            </Array>
          </mxGeometry>
        </mxCell>
      </root>
    </mxGraphModel>
  </diagram>
</mxfile>
rawio…]()


## Dependencias e instalación

### Instalación de Tkinter

Se inicia revisando la version de Python que se tiene con el comando:

```shell
python --version
```
Luego se revisa el PIP,

```shell
pip -V
```
Finalmente, se instala con el comando:

```shell
pip install tk
```


Otra forma de instalarlo es con:

```shell
sudo apt-get install python3-tk
```
### Implementación de gatito.py

Para que el programa ticTacToe.py funcione, se debe tener en la misma carpeta de descarga el archivo gatito.py, con que este programa esté en la carpeta junto a ticTacToe.py es suficiente para el éxito.

## Pasos para la ejecución

Ahora bien, para ejecutar el programa de manera correcta se debe asegurar de la instalación de sus dependencias. Luego, se debe accesar a la carpeta donde se descargó el archivo. Por último, para ejecutarlo se debe colocar el comando a continuación:


```shell
python3 ticTacToe.py
```


 
## Ejemplos de funcionamiento

A continuación se presenta cómo es que se ve el programa al ejecutarlo:

label cap2true:
    #bg salonclasestrue?

    "Desplazándonos para salir de la cafetería se sentía como si todos me siguieran, fui corriendo directo a un salón lejos de aquel lugar, entre todos bloqueamos la puerta una vez más."

    #show freya

    show freya normalhabla at center with dissolve:
        zoom sprite_size

    fr "Genial, ¿y ahora qué?"

    "Freya se veía poco satisfecha con el resultado obtenido, inclusive me miraba de forma molesta, como si tuviese culpa de que aquello hubiese funcionado."

    a "N... no lo sé."

    show freya ladohabla with dissolve

    fr "Bueno, esta fue tu elección, quizás tú deberías guiarnos, ¿no crees?"

    #show hanna

    show hanna miedohabla at left with dissolve:
        zoom sprite_size

    h "F...Freya, creo que estás siendo un poco dura..."

    show freya normalhabla with dissolve

    fr "¿Dura? Pudimos haber muerto por su indecisión."

    show hanna normal with dissolve

    h "Pero no estamos muertos, ¿o sí?"

    "El hecho de que fue su amiga hablando hizo que la chica de cabello negro respirase profundamente para calmar su enojo."

    show hanna explicano with dissolve

    h "Quizás deberíamos decidir qué haremos ahora..."

    #show evan

    show evan at left with dissolve:
        zoom sprite_size

    e "Eso si es que Freya quiere cooperar."

    fr "Oh, ¿así como tú ayudaste con la barricada?"

    "Evan se quedó quieto, quizás un poco más tieso de lo que debería de estar, como si un cubo de agua fría lo hubiese golpeado."

    h "Freya..."

    e "No, déjala Hanna, tiene razón."

    #hide evan

    "Evan se apartó del resto recostándose sobre una pared al otro extremo."

    #hide hanna, freya

    #show felix

    f "Es algo raro, ¿no crees?"

    "El chico de cabello rosa me preguntó viéndome atentamente."

    a "Debe tener sus razones."

    #show freya

    fr "Como sea, ¿qué hacemos ahora?"

    "Freya se cruzó de brazos, quizás estaba molesta por que no había elegido su forma de pensamiento, ¿si quiera eso es posible?"

    "Bueno, supongo que la gente se molesta si no se hace lo que ellos quieren."

    a "D...deberíamos regresar a la biblioteca."

    fr "No."

    #show hanna

    h "De hecho tiene un buen punto."

    "Hanna intentó interrumpir a Freya haciendo que la chica la mirara desconcertada."

    fr "¿Lo crees?"

    f "Sí, tiene sentido, si queremos saber más sobre el lugar, quizás deberíamos regresar a donde todo empezó."

    "Freya se veía muy poco convencida pero no le presté atención, mis ojos voltearon a Hanna quien se veía esperanzada por la idea."

    fr "Sí... supongo que tienen razón, pero, quiero que sepas que te advertí sobre esto."

    label cap2true_sideselection:

        #bg bibliotecatwilight

        "Todos me siguieron en silencio hasta la biblioteca, Evan nos seguía desde atrás, quizás muy atrás, eso me preocupaba ligeramente pero tampoco podía obligarlo a que me siguiese."

        "Al llegar a la biblioteca todos miramos a nuestro alrededor de forma curiosa y expectante, quizás algunos con más miedo que otros pero no había forma de averiguarlo."

        #show freya, evan, felix

        f "¿Qué estamos buscando?"

        a "Algo que nos saque de aquí, claro..."

        f "Deberíamos separarnos."

        "Quizás me vi un poco alterado por aquella sugerencia pero viendo que no íbamos a poder cubrir tanto espacio estando juntos asentí con la cabeza."

        e "Yo iré solo."

        #hide evan

        "Evan declaró antes de que pudiéramos decir algo y se dio la vuelta para meterse a algún pasillo."

        "Algo me dio un poco de nerviosismo, no sé si debería confiar en él, sobre todo con lo que acaba de ocurrir con la barricada."

        f "Podríamos separarnos todos y hacer una señal en caso de necesitar algo en particular, ¿quizás un silbido?"

        fr "Creo que si escuchamos un grito será suficiente."

        #hide freya, felix

        "Freya respondió de forma molesta dándose la vuelta para ir a investigar por su cuenta. Hanna y Felix asintieron con la cabeza dejándome solo."

        menu:
                "Vigilar a Evan":
                    call cap2true_evan from _call_cap2true_evan
                
                "Ayudar a Freya":
                    call cap2true_freya from _call_cap2true_freya

                "Acompañar a Hanna":
                    call cap2true_hanna from _call_cap2true_hanna

                "Ir con Felix":
                    call cap2true_felix from _call_cap2true_felix

    #bg bibliotecatwilight

    "Yo continué buscando entre los libros, quizás ya solo estaba moviéndolos entre ellos para ver si entendía alguno, pero nada, ninguno de los que movía parecía tener sentido alguno."

    "Pareciera magia, pero en uno de los libros tiré un papel doblado en múltiples partes, tal como el que estaba detrás de los posters de la cafetería."

    "Quizás es una pista, como el de la vez pasada."

    #bg pistaloki

    "Era una ilustración de Loki, el dios nordico, encerrado por varios círculos y siendo apuntado por varias flechas."

    "No entendía lo que quería decir..."

    #bg bibliotecatwilight w vpunch

    "Y como si fuese algo extremadamente importante, los chirridos de las ventanas comenzaron afuera, justo donde lo había visto la primera vez..."
    
    #bg bestiabiblioteca ?

    "Estaba el monstruo caminando con lentitud arañando las ventanas mirándome fijamente."

    h "¡¡AAAAAAAH!!"

    "Se escuchó cómo varios libros cayeron al suelo y pasos rápidos."

    h "¡FREYA! ¡¡FREYA!!"

    "Sin pensarlo dos veces corrí hacia donde estaban los demás reunidos."

    #show freya, hanna

    fr "¡Hay que irnos!"

    "Freya tomó la muñeca de Hanna cuando escuchó la ventana romperse en mil pedazos."

    #show felix

    f "¡La puerta!"

    #hide freya, felix, hanna

    "¿Cómo sabrían que no había una trampa? Por alguna razón mi corazón me decía que estaría bien, ¿era solo intuición, o el miedo inminente por la presencia del monstruo que ahora nos estaba acechando?"

    "Sin más, todos corrieron a la salida y cruzaron la misma sin problema alguno pero Hanna, Hanna se quedó dentro temblando."

    #show hanna, freya

    fr "¿¡Qué esperas Hanna!?"

    h "Los libros... ¡debo ir por ellos!"

    fr "¡¿QUÉ?! ¡NO!"

    h "¡¡Debo ir!! ¡Encontré algo, algo que tienen que ver!"

    #hide hanna

    "Hanna se dio la vuelta y corrió de regreso."

    fr "¡¡HANNA!!"

    #move freya to center

    #show evan

    "Su amiga intentó ir detrás de ella pero fue detenida por el agarre de Evan quien parecía estar temblando."

    fr "¡SUÉLTAME! ¡¡¡SUÉLTAME INUTIL!!!"

    e "Tienes que confiar en ella..."

    "Evan suplicó con la mirada."

    "Freya, aterrada, negó con la cabeza varias veces intentando soltarse del agarre del chico, sus ojos voltearon a la biblioteca" 
    
    #show hanna (small)

    "Y fue cuando vio a Hanna corriendo con los libros en sus manos."

    #hide hanna

    #show felix

    "Felix caminó dentro de la biblioteca extendiendo sus manos para que los lanzase."

    "Hanna no vio más opción y los lanzo haciendo que cayeran cerca de Felix, el cual comenzó a tomarlos"

    "Pero uno, uno que Hanna agarraba con fuerza entre sus manos, quizás aquel objeto material la había cegado por completo, tanto que tropezó con un par de libros que estaban tirados por el suelo."

    fr "¡¡HANNA!!"

    "Freya gritó una vez más."

    "No comprendo..."

    "No comprendo por que mi cuerpo no se mueve..."

    "Estoy aquí, parado, viendo cómo ocurre todo sin poder hacer nada."

    "¿Por qué Evan sostenía con fuerza la mano de Freya evitando que pudiese irse?"

    "No lo comprendo..."

    "Por qué... ¡¿por qué?! ¡¿POR QUÉ POR QUÉ POR QUÉ?!"

    #bg hannamuertetrue

    "Era tarde, el monstruo tomó el pie de Hanna y la arrastró por la librería."

    "Sus gritos y su miedo no pudieron despertar mi cuerpo paralizado, nada, nada de lo que intentaba estaba funcionando en absoluto."

    h "¡¡FREYA!!"

    "Se escuchó a la distancia, como un eco que se alejaba de mí, luego un grito escalofriante, seguido de un festival de sangre frente a los ojos de los demás."

    "Evan cubrió los ojos de Freya y la arrastró con sus fuerzas lejos de la escena mientras la chica gritaba, Felix cubría su boca aterrado."

    "Todo se volvió negro..."

    "No pude ver más..."

    #fade to black

    jump cap3true
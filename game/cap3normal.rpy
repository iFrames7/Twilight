label cap3normal:
    scene bg cap3normalscreen with Fade(1.0, 1.5, 1.0)

    pause 2.5

    scene bg pasillo2twilight with Fade(1.0, 1.0, 1.0)

    "Caminábamos a una velocidad apresurada."

    "No exactamente corriendo, pues todo estabamos exhaustos, pero tampoco caminando, ya que habíamos avistado la bestia."

    scene bg escaleras with dissolve

    "Freya camibana al frente y todos la seguíamos, tal como a un líder."

    "Optó por subir al segundo piso, poblado por salones de grados mayores, más clubes y, más importante, la oficina del rector; el cual era el objetivo."

    scene bg oficina with dissolve

    "Una vez llegamos, la mayoría nos sentamos para relajarnos un momento; a excepción de Freya."

    show freya normal at center with dissolve

    fr "Evan, quédate en la puerta y vigila que no venga esa bestia; mantén la puerta abierta, no queremos arriesgarnos."

    show freya ladohabla2 with dissolve

    fr "Hanna, tú vendrás conmigo, exploraremos el lado derecho de esta oficina."

    show freya caderaspreocupada2 with dissolve

    fr "Felix y... umm"

    show freya normalhabla with dissolve
    
    extend ", ¡AH!, Arden, ustedes dos busquen en el lado izquierdo de la oficina."

    show freya pensarhabla with dissolve

    fr "Recuerden buscar en cajones, debajo de sillas, mesas, lo que sea."

    show freya normal with dissolve

    fr "Destruyan la habitación si es necesario, pero hay que encontrar algo: alguna forma de salir de aquí, un arma de defensa, alguna otra pista bizarra, no lo sé."

    show freya ladohabla with dissolve

    fr "Nadie saldrá de aquí hasta que encontremos algo o ese monstruo nos obligue a salir."

    a "..."

    show felix normal at left 
    
    show hanna miedohabla at right

    show freya normal
    
    with dissolve

    f "..."

    h "..."

    hide hanna with dissolve

    show evan gimmeenojado at right with dissolve

    e "Oye, no sé si estuviste aquí hace unos minutos, pero pudimos haber muerto."

    show evan ladobrazoenojado with dissolve

    e "¿No crees que debamos procesar esto un rato antes de regresar inmediatamente al peligro?"

    show freya caderaspreocupada with dissolve

    fr "No tenemos tiempo de descansar, en cuanto bajemos la guardia algo más nos atacará y si no estamos listos podría ser nuestro fin."

    fr "Buscar una salida es la prioridad número uno."

    "Estaba de acuerdo con Evan, pero a la vez Freya hacía buenos puntos."

    "Si nos quedamos descansando solo extendemos el tiempo dentro de este mundo raro."
    
    "El descanso podía esperar hasta que estuviéramos sanos y salvos."

    show freya normalhabla with dissolve

    fr "Deja de quejarte y haz lo que te digo, avísanos si ves algo."

    show evan ladobrazo with dissolve

    e "Está bien, lo que tú digas."

    hide evan

    show freya sonrisahabla

    with dissolve

    "Evan caminó a la puerta, recargándose en ella y observando ambos lados."

    show hanna normal at right with dissolve

    show felix pensando2 with dissolve

    f "Debo decir, es raro que hayas querido venir a la oficina del rector, no sería mi primera idea y tampoco la de muchos."

    show freya pensarhabla with dissolve

    fr "Estar en el centro del segundo piso nos da buenas rutas de escape, podemos burlar a la bestia con las escaleras."

    show freya normalhabla with dissolve

    fr "Además, esta es la habitación con más libros y documentos después de la biblioteca."
    
    show freya caderassonrisa with dissolve

    fr "Estoy casi segura de que no solo habrá posters y notas inservibles aquí."

    show hanna emocionada with dissolve

    h "Wow, ¿y tú pensaste en todo eso antes de venir aquí?"

    show hanna emocionadahabla with dissolve

    h "Increíble."

    show freya sonrisahabla with dissolve

    "Su sonrisa lo decía todo."

    "Sip, definitivamente estaba orgullosa de eso."

    a "Quizás Freya tenga razón. Puede que los libros aquí no hayan cambiado mucho, o quizás tengan algo que nos ayude a salir de aquí."

    show hanna explicando with dissolve

    h "Ciertamente. El director debería tener algún mapa de la escuela, ¿no?"

    show hanna emocionada with dissolve

    h "Podemos buscar algo así por aquí."

    show felix sonrisahabla with dissolve

    f "Pues, no sé si encontremos algo así, pero haré lo que pueda."
    
    a "Sí, yo también."

    show freya normal 
    
    show hanna miedohabla

    show felix manofrentepreocupado
    
    with vpunch

    e "¡AHEM!"

    hide hanna

    show evan gimmeenojado at right

    with dissolve

    e "Creí que habías dicho que no hay tiempo de relajarse, ¿o sí?"

    show freya lado with dissolve

    fr "Tsk."

    show freya ladohabla2 with dissolve

    fr "Está bien, tienes razón."
    
    show freya normalhabla with dissolve

    fr "Todos, hagan lo que les toca."

    label cap3normal_sideselection:
        scene bg oficina 
        
        show felix sonrisahabla at center
        
        with fade

        "Tal y como Freya había ordenado, Felix y yo nos buscamos el lado izquierdo de la oficina."

        f "Yo iré por acá, tu checa por allá."

        a "Claro."

        hide felix with dissolve

        "Busqué por la sección más cercana a la puerta."
        
        "Había tanto mesas con cajones, los cuales contenían documentos legales sobre la escuela, su impartición y demás, y repisas que parecían interminables llenas de folders"
        
        "Todo contenía información variante, desde calificaciones hasta registros de alumno por letra, grado, y año; nada que pudiera parecer muy útil de momento."

        "Intenté buscar libros, diccionarios, mapas, etc., pero no estaba teniendo suerte."
        
        "Solo había más posters, documentos de poca utilidad y la ocasional nota ilegible."

        "Revisé alto y bajo, abriendo todos los cajones posibles, vaciándolos hasta que no hubiera más por leer, e incluso me subí a las mesas para ver las repisas más altas en caso de que hubiera algo de utilidad."

        "Hasta que eventualmente... "

        extend "me cansé."

        "Me senté en una silla para descansar y aclarar mi mente."

        a "{i}Haah...{/i}no sé qué hacer."

        "Voltee a ver a los demás."

        "Quizás ellos habían encontrado algo de utilidad."

        menu:
            "Acompañar a Evan":
                call cap3normal_evan from _call_cap3normal_evan

            "Hablar con Freya":
                call cap3normal_freya from _call_cap3normal_freya

            "Platicar con Hanna":
                call cap3normal_hanna from _call_cap3normal_hanna

            "Investigar con Felix":
                call cap3normal_felix from _call_cap3normal_felix

    scene bg oficina with fade

    "Tras aquella conversación, decidí continuar mi búsqueda."

    "Más cajones, más repisas, más documentos; ya estaba algo cansado."

    a "Hmm, sigo sin estar seguro de qué hacer."

    show felix sonrisahabla at center with dissolve

    f "Oye, no te rindas, si seguimos así encontraremos algo."

    a "Sí, eso espero."

    hide felix with dissolve

    "Me di la vuelta para contemplar la habitación un momento."

    show felix pensando2 at center with dissolve

    "Miré a ver a Felix haciendo lo mismo que yo."
    
    hide felix

    show freya angustiada at left

    show hanna miedohabla at right

    with dissolve

    "Volteé hacia Freya y Hanna, quienes parecían tener la misma suerte."

    hide freya

    hide hanna

    show evan ladobrazo at center

    with dissolve
    
    "Volteé a ver a Evan, seguía alerta, volteando hacia ambos lados y manteniendo la puerta en pie."

    hide evan with dissolve

    "Tras suspirar una vez más, me di cuenta del único lugar que nadie había observado: el escritorio del rector."

    "Me acerqué hacia ella."

    show felix ceja at center with dissolve

    f "Oye, ese es mi lado."

    a "Ya sé, solo dame un momento."

    hide felix with dissolve

    "La silla era enorme, demasiado como para que una persona se sentara ahí, y hecha de cuero, que parecía agregar más a la estética del asiento que a la comodidad."

    "Frente a ésta yacía un escritorio con 2 cajones encima de donde estarían las rodillas de quien se siente ahí, 2 cajones que no habían sido husmeados por nadie más."

    "Sin embargo, algo hizo click en mi cabeza y decidí buscar debajo del escritorio y del asiento primeramente."
    
    "No era la primera vez que veía una situación así."

    "Esta vez no encontré nada, al menos nada tan interesante como las otras veces, simplemente más posters y papeles ilegibles."

    "¿Será que nuestra suerte se estaba agotando?"

    a "Hmmm..."

    "Sin más, decidí abrir los cajones."

    "Éstos tenían manijas de metal con forma de leones; definitivamente muy llamativos para lo que eran."

    "Abrí el cajón lentamente y me encontré con lo esperado: más documentos, posters, papeles... "

    extend "hasta que algo inesperado cruzó mi visión."

    scene bg daga with dissolve

    "Una daga... "
    
    extend "una daga color negro con un cristal rojo."

    "La tomé en mis manos y la observé de cerca."

    "¿Qué era esta daga? ¿Qué hacía aquí? ¿Por qu-?"

    fr "Arden."

    scene bg oficina

    show freya preocupada at left

    show hanna despair at right

    with vpunch

    a "¡AHHH!"

    #sfx metaldrop

    "Tiré la daga al suelo."

    "Estaba tan concentrado que olvidé mis alrededores casi por completo."

    a "Ahh...lo siento, no las vi..."

    show freya normal

    show hanna normal

    with dissolve

    fr "¿Qué fue eso? ¿Qué ocurrió?"

    a "Oh, ummmm, sí, encontré est-"

    "Volteé a ver al suelo donde se encontraba la dagaque tiré, pero algo más llamó mi atención."

    "Había un pedazo de suelo desnivelado donde cayó la daga."

    "Detrás de este se encontraba un papel doblado."

    scene bg pistallave with dissolve #bg pistallave

    "Era una figura geométrica con forma de \"U\" pero cuadrado."
    
    "En la cima de la figura había lo que parecía un hoyo de cerradura de una llave y debajo de ella un dibujo de una daga."

    a "Huh..."

    scene bg oficina

    show freya normal at left

    show hanna normal at right

    with dissolve

    a "Freya..."

    a "Encontré esta daga en el cajón del rector, cuando cayó reveló esta imagen dentro del suelo"
    
    a "¿Qué crees que signifique?"

    show freya angustiada

    show hanna miedohabla

    with dissolve

    "Freya y Hanna se acercaron a observar cuidadosamente la daga."
    
    "Ambas parecían tan hipnotizadas por su diseño y su belleza como lo estuve hace unos momentos."

    show felix sonrisahabla at center with dissolve

    f "¿Lograron encontrar algo ustedes?"

    f "Yo solo vi unos cuantos papeles y- "

    show felix manofrentepreocupadohabla2 with vpunch

    extend "AHHH, ¡¿QUÉ ES ESO?!"

    show felix preocupado with dissolve

    f "UUUGH, no acerca eso a mí, ni de broma. ¿De dónde salió eso?"

    show freya angustiadahabla 
    
    show felix manofrentepreocupado
    
    with vpunch

    fr "CÁLLATE, no me dejas pensar."

    show freya normal with dissolve

    fr "La figura, no creo que signifique nada similar a las imágenes anteriores, no estoy segura de lo que sea."

    fr "Lo que sí puedo deducir es que esa daga debe ser algo importante."

    a "¿Qué te hace creer eso?"

    show freya ladohabla2 with dissolve

    fr "No hemos encontrado nada parecido a esto antes, ninguna habitación tenía dagas o algo por el estilo; debe significar algo."

    show freya normalhabla with dissolve

    fr "Además, el hecho de que en el dibujo la daga esté en frente del cerrojo me hace creer que puede ser nuestro boleto de salida."

    a "Pero...¿y si no es así?"

    show freya normal with dissolve

    fr "No lo sé, solo puedo confiar que quien sea que haya dejado todas estas imágenes esté de nuestro lado... "

    show freya angustiada with dissolve

    extend "No puedo garantizarte mucho más..."

    a "..."

    "Lo único que podemos hacer en esta situación es apegarse a la esperanza, ¿no es así?"

    "Nada garantizaba que estaremos seguros, lo único que podemos hacer era creer que lo estaremos."
    
    "Hasta ahora todo ha salido bien, pero nos hemos acercado al peligro más de lo que quisieramos."

    "¿Y si las cosas salían mal?"
    
    "¿Y si algún otro terminaba como... "
    
    extend "Katherine?"

    show freya normal with dissolve

    fr "Oye, Arden..."

    hide hanna

    hide felix

    with dissolve

    show freya at center with move

    fr "Deja de dudar."

    show freya normalhabla with dissolve

    fr "Solo limitas lo que puedes hacer; deja de hacerlo."

    show freya caderaspreocupada with dissolve

    fr "No puedo asegurar que estaremos bien, pero lograremos más haciendo algo que si nos quedamos aquí cuestionando si podemos hacer algo."

    show freya caderassonrisa with dissolve

    fr "No sé tú, pero yo quiero vivir, y lo mejor que puedo hacer ahora es confiar."

    show freya caderassonrisa with hpunch

    "Parpadeé un par de veces, sacudí la cabeza y me di unas palmadas en los cachetes."

    a "Sí, tienes razón."

    a "G-gracias, Freya..."

    a "Confiaré en lo que dices."

    show hanna normal at right with dissolve

    h "Oigan, ¿no es esa la forma de la escuela?"

    show freya preocupada with dissolve

    fr "¿Qué?"

    scene bg pistallave with dissolve #bg pistallave

    h "Sí, esa es la forma que tiene la escuela."

    h "Parece un imán de caricatura."

    h "Miren, la oficina del rector está aquí en el centro, y los dos pasillos que vigila Evan son estos."

    fr "Espera, creo que tienes razón..."

    fr "Asumiendo que esto sea un mapeo de la escuela, eso significa que..."

    a "La salida se encuentra al frente de la escuela."

    fr "Y la llave es esa daga."

    scene bg oficina

    show freya normal at left

    show hanna sonrisa at right

    with dissolve

    fr "No pierdas esa daga. Tenemos que llegar a la entrada de la escuela lo más rápido posible."

    a "Pero la salida estaba bloqueada, ¿recuerdas?"

    show freya normalhabla with dissolve

    fr "No fuimos a la del otro lado."

    a "...Tienes razón."

    show freya normalhabla with vpunch

    e "¡Chicos!"

    show evan gimmeenojado at center with dissolve

    "Evan interrumpió la conversación. Todos volteamos a verlo."

    e "Debemos irnos."

    show freya caderaspreocupada with dissolve

    fr "De acerdo, ¡vámonos!"

    jump cap4normal
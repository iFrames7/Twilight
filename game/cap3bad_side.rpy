label cap3bad_evan:
    scene bg oficina2 with Fade(0.3, 0.1, 0.3)

    show evan nmcigarlado at center with dissolve

    "Evan se encontraba en el marco de la puerta con un cigarro en la boca viendo hacia otro lado."

    "Cuando pude acercarme, pude ver una horrible cicatriz sobre su rostro."

    show evan nmnormal with dissolve

    "Al verme, Evan ocultó el cigarro y se encogió de hombros."

    e "Perdón, no te escuché llegar."

    a "N...No te preocupes ¿Estás bien?"

    show evan nmnormalhabla with dissolve

    e "Solo un poco estresado, siento que vamos en círculos y no encontramos nada."

    a "Sí, creo que yo también siento lo mismo..."

    "Hubo un pequeño silencio antes de que pudiese decir algo."

    a "¿Puedo... preguntar?"
    
    show evan nmcejahabla with dissolve

    e "No es muy agradable..."

    a "Ah...perdón, no quería molestar."

    show evan nmnormal with dissolve

    e "¡No! "
    
    extend "Ah"
    
    extend ", digo"
    
    extend ", no molestas."

    e "Es complicado hablar de esto... pero no es que pueda ocultarlo para toda mi vida."

    show evan nmcigarhabla with dissolve

    "Sacó nuevamente su cigarro antes de continuar."

    e "Mis padres no me querían del todo, si no fuera por las leyes del país quizás yo no existiría, y añádele el odio que le tendrían los familiares..."

    show evan nmcigarladohabla with dissolve

    e "Soy un niño no deseado, un niño no deseado de una familia adinerada, además de que nacer enfermo me hizo... ser mucho menos deseado, en serio no sé cómo es que sigo vivo."

    e "Esto..."

    "Evan apuntó a su rostro y bajo el cubrebocas para enseñar su cicatriz."

    e "Lo hizo mi madre, suena a un cliché de película... y no suele pasar a la gente adinerada..."

    a "Suena horrible..."

    show evan nmcigarladohabla2 with dissolve

    e "Lo fue..."

    e "Ocurrió cuando tenía 17 años más o menos... el gobierno me separó por abuso familiar pero... "
    
    extend "bueno"
    
    extend ", ¿qué diría el resto de la familia...?"

    show evan nmcigarnormal with dissolve

    e "Así que, con un par de sobornos y una buena cantidad de dinero me hicieron regresar a casa sin que nadie se enterara."

    a "Lo lamento mucho."

    show evan nmcigarhabla with dissolve

    e "Nada que lamentar."
    
    e "La gente con dinero es así... "

    extend "solo mueven las cosas cuando les conviene y cuando lo necesitan."

    "Se encogió de hombros nuevamente."

    a "Sí, supongo que sí... solo, no sabía... bueno..."

    show evan nmcigarlado with dissolve

    e "Hay muchas cosas que se quedan en las penumbras..."

    show evan nmcigarladohabla2 with dissolve

    e "Como sea, ahora mi propósito es robarles lo más que pueda de dinero, quizás así al menos pueda sacar algo de provecho."

    e "Lo bueno es que estoy estudiando lejos de casa y solo me mandan el dinero, puedo hacer lo que quiera."

    a "Eso es bueno..."

    show evan nmcigarladosonrisa with dissolve

    e "Sí, es lo mejor que me ha pasado"

    show evan nmcigarladohabla2 with dissolve
    
    e "¿Qué me dices de ti?"

    a "¿Yo? "
    
    extend "Oh"
    
    extend ", mi vida es muy aburrida, no creo poder decirte algo interesante la verdad."

    a "Bueno, mis padres son escritores, yo también..."

    a "Ammm, supongo que la barra está muy alta para mí... "
    
    extend "todos esperan que sea como ellos o quizás mejor..."

    show evan nmcigarhabla with dissolve

    e "Tsk, la sociedad haciendo de las suyas."

    a " Sí, supongo que sí... "
    
    extend "solo espero poder cumplir sus expectativas."

    show evan nmcigarladohabla with dissolve

    e "¿Quieres mi consejo?"

    e "No lo intentes, solo vivirás para los demás y nunca para ti mismo..."

    a "Yo... Lo tendré en cuenta... gracias..."

    return

label cap3bad_hanna:
    scene bg oficina2 with Fade(0.3, 0.1, 0.3)

    "Caminé hacia Hanna quien parecia sacar su celulares constaantemente para ver la localizacion del monstruo y tambien parecía tomar fotos de algunas cosas."

    show hanna normal at center with dissolve

    a "¿Qué haces?"

    show hanna sonrisa with dissolve

    h "Oh, nada realmente, solo me gusta tomarle fotos a todo lo lindo que veo, me ayuda a calmarme en situaciones así."

    a "¿Fotos? ¿No deberías guardar tu memoria en... momentos así?"

    show hanna miedohabla with dissolve

    h "Sí... supongo que sí... pero, en serio me gusta..."

    "Hanna se vio un poco triste al ver que le negue tomar fotos de alguna manera, quizas deberia arreglarlo."

    menu:
        "¿Y... a qué le tomas fotos?":
            a "¿Y... a qué le tomas fotos?"

            show hanna emocionada with dissolve

            h "Ah, mira, encontré esta pluma, debe ser de algun maestro, ¿no es linda?"

            "Era una pluma rosa con una especie de perrito sosteniendo una flor, era lindo."

            a "Sí, es linda, me pregunto a quién le pertenecerá."

            show hanna sonrisa with dissolve

            h "De quien sea, tiene un gusto excelente en detalles."

            a "Quizás cuando salgamos podríamos visitar al dueño para ver dónde la compró."

            show hanna emocionadahabla with dissolve

            h "¡Excelente idea!"

        "¿De qué sueles toma fotos?":
            a "¿De qué sueles toma fotos?"

            show hanna explicando with dissolve

            h "Oh, bueno, cuando veo algo que me gusta, como... flores... o quizás solo cosas bonitas, como... ah, como estas flores"

            show hanna emocionada with dissolve

            extend ", mira."

            "Hanna me mostró su celular y las fotos que tenía en él"
            
            "Tenía muchas fotos de ella y de Freya juntas, las cuales pareció pasar rapiamente antes de mostrarme fotos de flores y de pequeños conejos, todo muy adecuado a la temática de bonito."

            a "Son realmente bonitas."

        "¿Puedo... ver las fotos?":
            a "¿Puedo... ver las fotos?"

            show hanna emocionada with dissolve

            "Pareció que los ojos de hanna se iluminaron al escucharme y asintió con la cabeza."

            "Me mostro su celular y las fotos que tenia en él, tenía muchas fotos de ella y de Freya juntas, las cuales pareció pasar rapiamente antes de mostrarme fotos de flores y de pequeños conejos."
            
            "Todo muy adecuado a la temática de bonito."

            a "Tomas muy lindas fotos."

            show hanna emocionadahabla with dissolve

            h "Gracias, algun día espero poder comprarme una cámara solo para tomarle fotos todo lo que vea."

            a "Es una muy buena meta."

    show hanna sonrisa with dissolve

    "Hanna guardo su celular volteando a verme sonriente."

    h "Hey, a pesar de todo, me alegra haber sido encerrada con alguien como tú."

    a "¿Como yo?"

    show hanna explicando with dissolve

    h "Sí, como tú... eres... bueno, eres una persona que trae mucha paz, ¿sabes?"

    a "¿Mucha paz?"

    show hanna sonrisa with dissolve

    h "Sip."

    a "¿Cómo es eso?"

    show hanna explicando with dissolve

    h "Ah... no se como explicarlo... pero cuando estoy contigo al menos la preocupación se va un poco."
    
    show hanna emocionada with dissolve

    h "Es raro, ¿no lo crees?"

    a "No sé si sea raro... pero... Me alegra ayudar en algun sentido, supongo."

    show hanna emocionadahabla with dissolve

    h "Cuando salgamos, hay que hacer algo juntos."

    a "Me parece bien..."

    return

label cap3bad_felix:
    scene bg oficina2 with Fade(0.3, 0.1, 0.3)

    "Me acerqué a Felix quien tenía un libro entre sus manos, uno pequeño, pero eso no evitó que lo cerrase con fuerza al momento."

    #show felix

    show felix sonrisahabla at center with dissolve

    f "Oh, eres tú."

    a "¿Quién creías que era?"

    show felix manofrentepreocupado with dissolve

    f "Evan..."

    a "No parece agradarte, en ese caso."

    show felix normal with dissolve

    f "No es eso... bueno... tal vez un poco, es una persona muy seria y me aterra."

    a "¿Te aterra? Esa es una palabra un poco grave."

    show felix manofrentepreocupadohabla2 with dissolve

    f "Sí, supongo que sí, pero creo que es esa mirada, y... bueno, no sé, las personas poco sociables me suelen dar desconfianza."

    a "¿Cómo lo conociste?"

    show felix normal with dissolve

    f "¿A Evan?"

    show felix dedohabla with dissolve

    f "Katherine nos presentó hace mucho tiempo, pero fue una presentación únicamente formal... fuera de eso no hablamos mucho, Katherine era la que hacía todas las conversaciones."

    a "Ya veo... Bueno, no creo que sea mala persona..."

    show felix pensando2 with dissolve

    f "No, supongo que no..."

    a "¿Y cómo te sients?"

    show felix manofrenteceja with dissolve

    f "¿De qué? Estoy bien."

    a "De tu pie... te lo habías torcido, ¿no? Espero no te hayas hecho más daño mientras corríamos de un lado al otro."

    "Temí recordárselo, parecía que se le había olvidado."

    "Felix se veía desconcertado por la pregunta, como si no supiese de qué le estaba hablando."

    show felix normal with dissolve

    f "Mi..."
    
    extend "pie... "

    show felix sonrisahabla with vpunch
    
    extend "¡OH, OH! ¡Sí! "
    
    extend "No, no duele para nada, quizás solo fue cosa del momento pero está perfecto."

    a "Oh, ya veo."

    a "Bueno, eso es genial."

    a "Si en algún momento te cansas seria bueno que te sientes un rato, con eso de que la enfermería está cerrada no sé si sea bueno que sigas corriendo si estás lastimado."

    f "Lo haré, no te preocupes."

    return
label cap5true:
    #bg salon

    scene bg cap5screen with Fade(1.0, 1.5, 1.0)

    pause 2.5

    scene bg salonclases with Fade(1.0, 1.0, 1.0)

    play music "audio/plan.mp3" volume 0.25

    #show freya, evan

    show freya angustiada at left

    show evan pensando at right

    with dissolve

    fr "¿Y es lo único que podemos hacer?"

    "Freya suspiró cruzándose de brazos."

    "Millones de pensamientos comenzaban a vagar sobre las cabezas de todos, realmente no sabíamos qué hacer."

    show evan despair with dissolve

    e "No tenemos otra opción, ¿o sí?"

    a "No me gusta"
    
    extend ", de hecho me aterra."

    "¿No había la simple opción de cantar un par de alabanzas y que los dioses nos protegieran?"

    show evan gimmeenojado with dissolve

    e "Bueno, pero no creo que haya mejores opciones, al menos no por el momento."

    "Freya asintió con la cabeza de forma asertiva, se levantó y nos miró."

    show freya normalhabla with dissolve

    fr "Por mucho que deteste la idea, es lo único que podemos hacer si queremos salir con vida y esperar que nadie más pase por esto."

    show freya caderashabla with dissolve

    "Sus brazos se colocaron sobre sus caderas con seguridad."

    fr "Bien, supongo que deberíamos separarnos..."

    show evan lado2 with dissolve

    e "No veo otra opción..."

    "Estos tomaron las páginas del anuario y analizaron con cuidado su contenido."

    "Era una serie de instrucciones para poder encontrar la daga. Ésta estaba escondida en un cajón de la oficina principal, todo se veía bastante sencillo"
    
    extend "... en papel."

    a "¿Cómo nos dividimos?"

    show freya pensarhabla with dissolve

    fr "Bueno..."

    "Freya volteó a ver a Evan."

    show freya apuntaceja with dissolve

    fr "¿Hay algo que quieras decir antes de continuar?"

    show evan normal with dissolve

    e "¿Algo?"

    show freya apunta2 with dissolve

    fr "Sí... No queremos que no hagas tu trabajo por alguna excusa que pongas."

    "Evan bajó la mirada, avergonzado."

    show evan defensivo with dissolve

    e "Yo... ammm... No creo poder hacer mucho esfuerzo... sufro de... múltiples condiciones."

    show evan ladobrazo with dissolve
    
    e "Puedo ayudarlos en lo que sea que no tenga que ver con algo físico."

    if not evan_cap4_talk:
        "Ladee mi cabeza."

        "No comprendo por qué esperó hasta ahora para decirnos eso."

        "Debe tener sus razones, supongo."

    a "Eso es un problema..."

    a "Bueno, yo puedo ir a buscar la daga... Freya puede ir a buscar el libro."

    show evan gimmeenojado with dissolve

    e "Podría distraer al monstruo, quizás no me pueda mover mucho pero conozco trucos que funcionan con animales grandes como osos y tigres."

    show evan normal with dissolve

    e "Sería probar la suerte... pero les daría suficiente tiempo para preparar todo."

    "Evan sonaba convencido."

    a "Suena riesgoso..."

    show evan gimme with dissolve

    e "Pero útil."

    "Freya lo miró con preocupación."

    show freya angustiada with dissolve

    fr "¿Seguro que quieres hacerlo?"

    show evan normal with dissolve

    e "Si puedo ser de utilidad... lo haré."

    show freya caderaspreocupada with dissolve

    fr "Entonces confiamos en ti."

    a "Bien, supongo que podemos dar una señal cuando estemos listos... podríamos encontrarnos todos en el tejado..."

    show evan gimme with dissolve

    e "Suena bien."

    show freya normal with dissolve

    fr "Concuerdo."

    show freya apunta2 with dissolve

    fr "¿Falta algo?"

    "Evan y yo negamos con la cabeza, haciéndole saber que estábamos listos."

    show freya angustiada with dissolve

    fr "Pues más les vale no morir, o se arrepentirán por el resto de la eternidad."

    "No sabía si era un chiste o una amenaza, pero preferí no pensarlo y correr a donde me correspondía."

    "Evan y Freya hicieron lo mismo."

    stop music fadeout 0.5

    #bg oficina

    scene bg oficina with Fade(0.3, 0.3, 0.3)

    play music "audio/creepingdevil.mp3" volume 0.25

    "Busque ambos lados de la habitación al entrar."

    "Examiné cada esquina de la oficina."

    #choices que te regresan hasta agotarse, idk, algo cool

    "Al revisar uno de los cajones al fondo, encontré lo que buscaba."

    #bg daga ?
    
    scene bg daga with dissolve

    "Una daga color negro con un cristal rojo."

    "Algo sobre ella... me mantenía interesado."

    "La miré por unos segundos, apreciando su hipnotizante belleza."

    "Realmente era... "

    extend "una obra de arte."

    #bg oficina

    scene bg oficina with vpunch

    stop music fadeout 0.5

    "Sacudí mi cabeza, rompiendo con aquella distracción."

    a "Aghh... No es tiempo para esto."

    "La realidad de la situación me hizo volver a estar alerta."

    "Coloqué la daga en el bolsillo de mi sudadera, acompañado de un terrible escalofrío."

    #bg pasillo

    scene bg pasillo2twilight with dissolve

    "Intentando ser veloz, salí de la oficina en cuanto obtuve la daga."

    "Mas al salir y subir la mirada, me pude encontrar con Felix."

    play music "audio/murderer.mp3" volume 0.15

    #bg evilfelix

    show efelix normal at center with Dissolve(1.5)

    play sound "sfx/heartbeat.mp3" volume 0.75 loop

    "Esa sonriza amenazante..."

    "La saliva negra brotando de su boca..."

    "Los tatuajes y símbolos en sus brazos..."

    "Todo ello me atemorizaba."

    "No podía moverme"

    extend ", justo como aquella vez..."

    show efelix habla with dissolve

    ef "Arden..."

    "Su voz maquiavelica alcanzó mis tímpanos."

    "Seguía completamente paralizado... "

    stop sound fadeout 1.5

    extend "hasta que sentí la daga en mi bolsillo."

    "Me aferré a ella."

    a "F...Felix."

    #bg pasillo

    #show efelix

    show efelix brazos with dissolve

    ef "¿Te cansaste de jugar conmigo, Arden?"

    "Era una voz vacía, como si millones de almas gritasen en su interior."

    "Era escalofriante, me aterraba demasiado."

    a "¿Esto... es un juego para ti?"

    show efelix habla with vpunch

    ef "¡JAJAJAJAJAJAJA!"

    show efelix dientes with dissolve

    ef "Claro que lo es, pequeños ratoncillos en una jaula esperando ser devorados por un gran gato que los vigila."

    a "¡¿No tuviste suficiente con Katherine?! ¡¿Con Hanna?!"

    "Estaba intentando ser fuerte."

    show efelix brazos with vpunch

    ef "No, necesito más, ¡necesito mucho más!"

    "Si nuestras teorías eran ciertas, quiere decir que si no nos mató antes fue por alguna razón."

    "Me armé de una cantidad inmensa de valor, una que realmente no sé de dónde salió."

    "Seguía temblando, mas comencé a avanzar hacia Felix."

    "Sentía que caminaba hacia mi muerte, pero no me detuve."

    a "No puedes hacerme daño... ¿cierto?"

    a "No puedes tocarme... por que tu cuerpo no pertenece a este mundo..."

    show efelix normal with dissolve

    "Felix comenzaba a retroceder lentamente, su expresión me decía que había dado en el blanco."

    a "Es por eso que usas a la bestia... está conectada a ti..."

    show efelix manoboca with dissolve

    ef "¿C-cómo-...?"

    a "Porque yo... ¡voy a ser quien acabe contigo!"

    show efelix normal with vpunch

    "Sin pensarlo dos veces, le lancé a la cabeza un bote de basura que se encontraba cerca."

    "No esperaba hacerle ningún daño, solo causar una distracción, la cual fue suficiente para salir corriendo."

    #hide efelix

    scene bg pasillo3twilight with dissolve

    "A lo lejos escuché una risa maniaca."

    show bg pasillo3twilight with vpunch

    ef "¡ESTE LUGAR ME PERTENECE!"

    scene bg pasillotwilight

    "Seguí corriendo sin mirar atrás."

    "Los pasillos comenzaron a volverse viscosos. "

    extend "Mi nombre estaba siendo gritado y resonaba en todos lados. "

    extend "Podía ver de reojo a sombras que me seguían, humo que comenzaba a nublar mi vista."

    #choice de dirección? debatible, explica tu razonamiento tho

    #bg escaleras

    scene bg escaleras with dissolve

    "Hice un derrape a través de los pasillos y continué mi trayecto, dando todo de mi ser para correr."

    "Subí las escaleras rápidamente y me preparé para llegar al tejado."

    "Felix había jugado suficiente con su comida, pero ya no más, no lo permitiré."

    #bg techo

    stop music fadeout 0.5

    scene bg techo with dissolve

    play sound "sfx/1doorbang.mp3" volume 0.75

    "Abrí la puerta con fuerza"

    extend ", tanto que mi cuerpo rodó por el suelo y se mantuvo ahí."

    play sound "sfx/heartbeat.mp3" volume 0.75 loop

    "Mi respiración estaba entrecortada, mis manos temblando, mi corazón palpitando."

    "El miedo me llenaba, pero esta vez no me consumía."

    "Escuché un fuerte ruido por donde vine."

    "Se estaba acercando..."

    fr "¡Arden!"

    stop sound fadeout 0.5

    #cut a freya pov

    #bg pasillo

    scene bg pasillotwilight with Fade(0.5, 0.5, 0.5)

    play music "audio/mysterious.mp3" volume 0.25

    fr "Tú puedes, tú puedes..."

    "Me repetía a mí misma mientras caminaba hacia mi destino."

    "La biblioteca... "

    extend "el lugar donde Hanna..."

    play sound "sfx/1heartbeat.mp3" volume 0.75

    show bg hannamuerte with Dissolve(0.25)

    show bg pasillotwilight with Dissolve(0.25)    

    fr "Ugh."

    "No sé si me atemoriza más encontrarme a la bestia o tener esa imagen en la cabeza."

    "Pero no es tiempo de pensar en ello."

    "Hay cosas más importantes ahora."

    "Una vez llegué a la biblioteca me detuve un segundo."

    fr "{i}Sighhhh{/i}"

    fr "Debo entrar."

    #bg biblioteca

    scene bg bibliotecatwilight with dissolve

    "Al entrar, inmediatamente noté la sangre en el suelo."

    play sound "sfx/1heartbeat.mp3" volume 0.75

    show bg hannamuerte with Dissolve(0.25)

    show bg bibliotecatwilight with Dissolve(0.25)   

    "Seguramente era la sangre de Hanna cuando el monstruo la arrastró."

    play sound "sfx/1doorbang.mp3" volume 0.5

    scene bg bibliotecatwilight with vpunch #para mostrar efecto de que golpea algo

    fr "Demonios..."

    fr "Evan, maldito infeliz..."

    fr "Si tan solo hubiera..."

    "Apreté el puño con fuerza pero..."

    fr "..."

    fr "..."

    fr "No..."

    "Ahora lo sabemos. "

    extend "Sin el ritual, no podemos derrotar a la bestia."

    "Sería inútil haber intentado algo."

    fr "Hanna..."

    "Evité ver seguir pensando y corrí hacia el otro lado de la habitación."

    scene bg bibliotecatwilight2 with dissolve

    play sound "sfx/papers.mp3" volume 0.75

    "Justo como Arden había dicho, entre la alfombra y la entrada principal, había un libro."

    fr "Wow."

    "Seguía pareciéndome increíble que ese chico pudiera comunicarse con espíritus."

    "Pero ahora había una prueba física de que sí podía."

    "Le di una leída rápida, encontrándome nuevamente con esos símbolos extraños, pero no pensé mucho en ello."

    fr "No queda mucho tiempo."

    "Ahora solo debía correr..."

    stop music fadeout 0.75

    "..."

    scene bg bibliotecatwilight with dissolve

    "Habiendo solo una salida, volteé hacia ella y nuevamente me topé con ese incómodo sentimiento... "

    play sound "sfx/1heartbeat.mp3" volume 0.75

    show bg hannamuerte2 with Dissolve(0.25)

    show bg bibliotecatwilight with Dissolve(0.25)   

    extend "y esa incómoda escena."

    fr "..."

    "Volteando a ver el charco de sangre, había algo en medio."

    "Un libro... "

    extend "probablemente "

    extend "el libro por el cual Hanna arriesgó su vida."

    fr "..."

    "Me acerqué hacia él y lo tomé en mis manos."

    "Lo abrí y comencé a examinarlo."

    "Era una especie de diccionario. Contenía los símbolos que hemos visto anteriormente en otros libros o posters y los ponía de una manera más interpretable."

    play music "audio/intimate.mp3" volume 0.5

    fr "No puede ser..."

    "De pronto tuvo sentido."

    "Hanna había encontrado esto y sabía que sería útil."

    "Abrí el libro con el ritual y comencé a traducir ciertas secciones con el diccionario."

    fr "Dios mio..."

    fr "Este libro contiene todo."

    "Había mucha información sobre el mundo y sus propiedades, maneras de escapar y demás."

    fr "Hubiera sido increíble saber sobre esto antes."

    "Llegando a la sección del ritual, una tiza negra cayó del libro, la cual podía usar para dibujar los símbolos."

    fr "Bien."

    "Lo único que necesitaba era tiempo."

    "Me levanté rápidamente, tomando ambos libros y sosteniéndolos fuertemente contra mi pecho."

    "Antes de correr, noté que una pequeña nota cayó del diccionario, tenía algo escrito en ella."

    show hanna sonrisa at center with dissolve:
        alpha 0.49 

    "\"No es tu culpa, te amo...{p}- Hanna.\""

    hide hanna with dissolve

    fr "..."

    fr "..."

    "Eso... "

    extend "fue lo que me tiró sobre la barda."

    "Mi rostro se llenó de lágrimas."

    "Puede que esté loca, pero en ese momento podía sentirla... "

    extend "a Hanna, aquí conmigo."

    "Quizás es ella la que me está ayudando a escapar..."

    fr "{size=-6}Gracias, Hanna...{/size}"

    "Salí corriendo hacia la azotea."

    stop music fadeout 1.5

    #bg techo

    scene bg techo with Fade(0.3, 0.1, 0.3)

    "El viento soplaba fuertemente, mi cabello se movía violentamente."

    scene bg techo2 with dissolve

    "Coloqué mis pies firmemente en el suelo y comencé a trazar el ritual."

    play sound "sfx/1doorbang.mp3" volume 0.75

    "Al terminar, escuché un fuerte ruido y la puerta abriéndose."

    "Era Arden, tirado en el suelo."

    fr "¡Arden!"

    #cut a arden pov

    #bg techo

    scene bg techo2 with Fade(0.5, 0.5, 0.5)

    play music "audio/creepingdevil.mp3" volume 0.25

    "Freya me gritaba a lo lejos."

    #show freya

    show freya preocupada at center with dissolve

    fr "¿Estás bien Arden?"

    a "Debemos irnos, si no..."

    #show felix

    show freya at right with move

    show efelix habla at left with vpunch

    ef "¡SÍ NO QUÉ!"

    "Felix ya se acercaba, su cuerpo entero derramaba líquido color negro."

    "Me levanté y caminé hacia atrás."

    "Freya hacía lo mismo."

    ef "¡¿QUÉ HARÁN TÚ Y TUS AMIGOS?!"

    show efelix normal with dissolve

    "Su imagen era perturbadora, lo único que había en mi ser era miedo."

    show freya angustiada with dissolve

    fr "..."

    show freya angustiadallora2 with dissolve

    fr "Por qué..."

    fr "¿Por qué haces esto?"

    show freya angustiadahablallora with vpunch

    fr "¡¿POR QUÉ MATASTE A MI AMIGA?!"

    "Felix rió fuertemente."

    show efelix brazos with dissolve

    ef "Un simple sacrificio... por un bien mayor."

    show freya angustiadahablallora3 with dissolve

    fr "¿Un bien mayor?"

    show freya angustiada with dissolve

    "Freya apretó los puños fuertemente."

    fr "Mientes... "

    show freya angustiadahabla with vpunch

    extend "¡MIENTES!"

    show efelix habla with vpunch

    ef "{size=+10}JAJAJAJAJAJAJAJAJA{/size}"

    a "¡Ya basta!"

    show efelix dientes with vpunch

    ef "NO SE PREOCUPEN, LES DARÉ LA MEJOR MUERTE QUE PUEDAN TENER."

    scene bg black with dissolve

    stop music fadeout 2.5

    "Ya basta..."

    "Ya había sido suficiente."

    a "Esto se acaba ahora..."

    "Metí mi mano en mi bolsillo para agarrar la daga."

    "..."

    "..."

    "... "

    extend "nada..."

    scene bg techo2

    show efelix dientes at left

    show freya angustiada at right

    with dissolve

    "No había nada..."

    a "..."

    "No había nada en mi bolsillo, no encontraba la daga, no sentía nada."

    "¿Cuándo se perdió? ¿Fue cuando corría? En el pasillo, debe estar en el pasillo."

    #sfx de la bestia

    play sound "sfx/beast1.mp3" volume 0.5

    show bg techo2 with vpunch

    "Mirando a lo lejos, el monstruo que se supone que Evan estaba distrayendo se encontraba destruyendo la puerta hacia el techo."

    play sound "sfx/heartbeat.mp3" volume 0.75 loop

    "No..."

    "No..."

    "No puede ser..."

    a "Evan..."

    "¿Estaba ahí dentro? ¿Todavía estaba vivo?"

    "No podía moverme, mi corazón comenzaba a palpitar fuertemente."

    play music "audio/murderer.mp3" volume 0.25

    show efelix brazos with dissolve

    ef "Está muerto, no creo que quieran esperarlo."

    a "No..."

    a "Mientes."

    show efelix manoboca with dissolve

    ef "¿Y qué te hace creer que miento?"

    show bg techo2 with vpunch

    a "{size=+6}¡¡MIENTES!!{/size}"

    stop sound fadeout 0.5

    "Con lágrimas en los ojos, lo único que podía hacer era negarlo."

    "Todo el plan comenzaba a desmoronarse."

    "Sin la daga no podemos hacer nada..."

    #sfx bestia

    scene bg beast2 with dissolve

    scene bg beast2 with vpunch

    play sound "sfx/beast2.mp3" volume 0.5

    "La bestia comenzó a correr hacia nosotros, mas se detuvo en el círculo."

    "Éste comenzó a brillar fuertemente, deteniendo a la bestia."

    scene bg techo2

    show efelix dientes at left

    show freya angustiadahabla at right

    with dissolve

    show freya angustiadahabla with vpunch

    fr "¡Arden, la daga!"

    a "..."

    show freya preocupada with dissolve

    "Solo pude voltear a verla, las lágrimas derramándose de mi cara."

    "No pude lograr decir una sola palabra."

    show efelix brazos with dissolve

    ef "Oh, ¿esta daga?"

    "Felix sostenía en su mano la daga que yo tenía antes."

    ef "¿Sabías que es malo correr por los pasillos de la escuela?"

    show freya angustiada with dissolve

    fr "Arden..."

    stop music fadeout 1.0

    a "Freya... yo... lo siento..."

    a "Lo lamento... No debí... No debí creer que... podía hacer algo por los demás."

    scene bg black with dissolve

    "No sé qué hacer..."

    "No sé si podemos hacer algo, no sé si puedo hacer algo..."

    "Quizás nunca debí de haber tomado la iniciativa desde el principio..."
    
    "No"
    
    extend ", ni siquiera debí de intentarlo..."

    e "¡¡ARDEN!!"

    a "¿...?"

    #cut a evan pov

    #bg pasillo

    scene bg pasillo3twilight with Fade(0.5, 0.5, 0.5)

    play music "audio/creepingdevil.mp3" volume 0.25

    e "{i}Hah...Hah...Hah...{/i}"

    "Mi respiración estaba entrecortada."

    "No estoy hecho para esto."

    "Y con el añadido de que estoy muriéndome de miedo... "

    extend "realmente estoy tirándo un dado y depeniendo de él."

    "El laboratorio está por aquí."

    "Quizás ahí encuentre los tranquilizantes para animales."

    #sfx bestia

    play sound "sfx/beast1.mp3" volume 0.5

    show bg pasillo3twilight with vpunch

    e "Ugh..."

    "Ese horrible gruñido... "

    extend "definitivamente viene del pasillo."

    "Me asomé cuidadosamente sin hacer mucho ruido."

    #bg bestia

    scene bg beastclose with dissolve

    "Claro."

    "Era tan espelusnante como la recordaba."

    "En serio espero que esto funcione..."

    #bg pasillo

    scene bg pasillo3twilight with dissolve

    "Saqué un láser de mi bolsillo y lo apunté al final del pasillo, moviéndolo bruscamente para llamar su atención."

    #sfx bestia

    play sound "sfx/beast1.mp3" volume 0.5

    scene bg pasillo3twilight with vpunch

    "El monstruo se vio más molesto que interesado, comenzó a gruñir fuertemente."

    "Esperé a que estuviera completamente volteado para ejecutar mi maniobra..."

    stop music fadeout 0.5

    "..."

    "..."

    e "Ahora."

    "Sin pensarlo, corrí lo más rápido que pude hacia el laboratorio."

    #bg monstruo

    scene bg beastfrente2 with dissolve

    play sound "sfx/beast2.mp3" volume 0.5

    "No sin antes ser amenazado con la vista del monstruo."

    e "Mierda..."

    #bg lab

    scene bg lab with dissolve

    "Por fortuna, los tranquilizantes estaban en un lugar accesible."

    "Una caja encima de los escritorios; todo justo como estaba antes de que llegaramos a este mundo."

    "Corrí hacia ellos."

    "Sentía la presencia de la bestia detrás mio, por lo que aceleré el paso."

    scene bg lab with vpunch

    play sound "sfx/fall.ogg" volume 0.75

    e "¡AGH!"

    "Sí, podía sentirlo."

    "Mis pasos se alentaban y mi cuerpo no podía mucho más."

    "Me tropecé y caí, no sin antes tirar la caja que buscaba, esparciendo los tranquilizantes a través de todo el suelo."

    e "¡Gah!... Mierda..."

    play sound "sfx/heartbeat.mp3" volume 0.75 loop

    "El monstruo se acercaba lentamente hacia mí."

    #bg bestia

    scene bg beast2 with dissolve

    "Éste se colocó encima de mí."

    "Comenzaba a soltar zarpazos, intentando rasgar mi cara."

    "Solo pude bloquearla con mis patéticos brazos."

    scene bg beastclose with vpunch

    play audio "sfx/beast2.mp3" volume 0.5

    e "¡¡AAAAAAAAAAAAAAAAAHHHH!!"

    "O al menos lo intentaba."

    scene bg beastfrente2 with vpunch

    play audio "sfx/beast1.mp3" volume 0.5

    "Sus garras atravesaban mi piel con facilidad."

    "La sangre se derramaba en toda mi cara."

    scene bg beastfrente with vpunch

    #Maybe hacer un efecto cool aquí

    "¿Realmente era este mi fin?"

    "¿Moriré aquí...?"

    scene bg beastfrente with vpunch

    play audio "sfx/beast1.mp3" volume 0.5

    e "¡¡GAAAAAAAAAAAAAAAAAHHH!!"

    "...No."

    "Hay gente que cuenta conmigo ahora."

    "No puedo morir aquí, no debo morir aquí..."

    #bg lab

    scene bg lab with dissolve

    "Desesperado, tomé una de las jeringas en el suelo."

    scene bg lab with vpunch

    e "¡¡¡RAAAAAAAAAAAAAAAGHHHHH!!!"

    play audio "sfx/blood.mp3" volume 0.4

    "Y la clavé directamente en el cuello de la bestia."

    #sfx de bestia

    play audio "sfx/beast1.mp3" volume 0.5

    scene bg lab with vpunch

    "La bestia se retorció momentáneamente, dándome una oportunidad de correr."

    "No lo pensé dos veces antes de salir corriendo."

    #bg pasillo

    scene bg pasillo3twilight with dissolve

    "Seguí corriendo."

    "Solo corría hacia donde mi cuerpo me llevara."

    "No podía gastar energía en pensar, solo en correr."

    #bg escalera

    scene bg escaleras2 with dissolve

    stop sound fadeout 0.5

    "Subí al segundo piso en busca de más refugio, pero al llegar a la cima de las escaleras, mi cuerpo se rindió."

    e "{i}Hah... Hah... Hah... Hah...{/i}"

    "Me recargué en una pared y respiré profundamente."

    e "{i}Hah... {/i}"

    extend "{i}Hah... {/i}"

    extend "{i}Hah... {/i}"

    extend "{i}Hah...{/i}"

    scene bg escaleras2 with vpunch

    e "¡AUCH!"

    "Fue ahí cuando noté el inmenso dolor en mis brazos."

    "Es interesante cómo funciona la adrenalina."

    scene bg escaleras2 with vpunch

    e "¡GAAH-...!"

    "Era difícil intentar moverme."

    e "¡MMM...! "

    extend "No"

    extend ", esto aún no se acaba."

    #sfx pisadas

    play music "audio/mysterious.mp3" volume 0.25

    "En cuanto pensé eso, escuché unas pisadas apresuradas y un sonido como si miles de gritos fueran escuchados al mismo tiempo."

    "Me oculté en las escaleras y me asomé cuidadosamente para ver lo que ocurría."

    "Era Arden, corriendo hacia el techo. "

    extend "Y una figura malevola, la cual asumo que era Felix, persiguéndolo."

    e "Heh... parece ser que todo va en orden."

    play sound "sfx/metaldrop.mp3" volume 0.5

    "Un sonido de metal resonó en los pasillos."

    "Al asomarme, noté que era la daga, la cual cayó del bolsillo de Arden, mas él no se dio cuenta y siguió en su trayecto."

    ef "¿Huh?"

    "Felix se detuvo a observarla e intentó tomarla."

    scene bg escaleras2 with vpunch

    play sound "sfx/GodShift2.wav" volume 0.9

    ef "¡GAAAHHH!"

    "Su cuerpo entero se apartó con un grito de dolor, su mano se había quemado al intentar tocarla."

    ef "Hmph."

    "Felix continuó su trayecto."

    #bg pasillo

    scene bg pasillo3twilight with dissolve

    "Salí de mi escondite y caminé hacia la daga."

    e "Vaya, entonces realmente funciona..."

    "La sostuve con ambas manos, admirando momentáneamente su belleza."

    stop music fadeout 0.5

    play sound "sfx/beast2.mp3" volume 0.5

    "Mis pensamientos fueron interrumpidos por un fuerte gruñido."

    #bg bestia

    scene bg beast with dissolve

    "Subí la mirada y al fondo del pasillo vi a la bestia."

    "Salté un poco del miedo, pero rápidamente me di cuenta que yo no era su objetivo."

    #bg pasillo

    scene bg pasillo3twilight with dissolve

    "Ésta corría rápidamente hacia el techo, tomando el mismo trayecto que Felix y Arden llevaban."

    e "..."

    e "Van a necesitar esto."

    "Caminé rápidamente hacia el techo, ignorando todo dolor y señal de peligro que mi cerebro me alertaba."

    "No. "

    extend "Aún no se acababa esto."

    #cut a arden pov

    #bg techo

    scene bg techo 

    show evan nmlastimadoenojado at center

    with Fade(0.5, 0.5, 0.5)

    "Estaba sangrando, su cuerpo entero lleno de rasguños pertenecientes a la bestia."
    
    "Sin embargo, en su mano izquierda tenía la daga, la daga que Felix estaba sosteniendo."

    show evan nmlastimadoangustiado with vpunch

    e "¡¡ARDEN!!"

    a "¿...Qué?"

    "La daga de Felix... "

    extend "¿era falsa?"

    scene bg techo2 
    
    show freya preocupada at right

    show efelix dientes at left
    
    with dissolve

    "Evan lanzó la daga hacia mí."

    "Sin pensarlo dos veces, corrí hacia ella."

    "Felix intentó interceptarla, pero su piel comenzó a quemarse cuando intentó tocarla."

    "Atrapé la daga y aproveché la situación para correr hacia Felix."

    #bg ardenfelixcuchillo

    scene bg ardenfelixcuchillo with dissolve

    scene bg ardenfelixcuchillo with vpunch

    a "¡RAAAAAAAAAAAAAHHHH!"

    "Me acerqué hacia él, lo tomé del cuello y lo empujé fuertemente."

    #bg ardenfelixcuchilloenterrado

    play sound "sfx/guillotine.mp3" volume 0.5

    scene bg ardenfelixcuchilloenterrado with vpunch

    "Y enterré la daga en su cuello."

    "Sangre, mucha sangre comenzó a brotar. "

    extend "Gritos de millones de almas que habían muerto"

    extend ", el grito horripilante de Felix."

    "Miles de pensamientos llenaban mi cabeza."

    scene bg ardenfelixcuchilloenterrado with vpunch

    ef "¡¡AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAGH!!"

    "La daga estaba siendo rechazada por el cuerpo de Felix."

    "Estaba siendo repelada por toda la oscuridad en su ser."

    "Mantuve firme mi agarre y empujé aún más fuerte."

    "Y de pronto... "

    #bg white

    #sfx white noise

    play sound "sfx/earringing.mp3" volume 0.75

    scene bg white with Dissolve(2.0)

    extend "blanco..."

    "Y un sonido que penetraba mis oidos."

    "{i}Biiiiiiiiiiiiiiiiiiiiiiiiiiiiip{/i}"

    "..."

    "..."

    "..."

    "...No podía ver nada..."

    "...¿Lo logramos?"

    "...¿Se había terminado todo?"

    "Todo comenzó a aclararse."

    #bg techonormal

    scene bg techo2azul with Dissolve(1.75)

    "La luz de la luna los estaba iluminando, una luna roja pero el cielo azul."

    "¿Estamos de regreso?"

    "Miré a mi alrededor."

    play music "audio/ending.mp3" volume 0.5

    fr "¡ARDEN!"

    "Freya corría hacia mí para ayudarme."

    #show freya

    show freya angustiadahablallora2 at center with dissolve

    fr "Arden, ¿estás bien?"

    a "Freya..."

    a "¿Lo hicimos?"

    e "Lo hicimos..."

    "Detrás de mí sonó la voz de Evan."

    #show evan

    show freya at right with move
    
    show evan nmlastimadonormal at left with dissolve

    "Caminó lentamente hacia nosotros para abrazarnos."

    scene bg abrazofinal with dissolve

    a "¡EVAN!"

    a "¡ESTÁS SANGRANDO!"

    e "Solo un poco..."

    fr "¡HAY QUE LLAMAR A UNA AMBULANCIA!"

    e "Estoy bien..."

    fr "¡¡No lo estás!! ¡Dejame verte!"

    stop music fadeout 2.5

    scene bg black with Fade(1.5, 0.5, 0.5)

    pause 1.5

    jump epilogotrue
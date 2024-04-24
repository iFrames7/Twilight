label cap3true:
    $ codigo_real = 4869

    #bg dream2 ?

    scene bg cap3screen with Fade(1.0, 1.5, 1.0)

    pause 2.5

    scene bg dream2 with Fade(1.0, 1.0, 1.0)

    play music "audio/nightmare.mp3" volume 0.25

    "Nuevamente, estoy en este vacío..."

    "Pero puedo ver a más personas... "

    extend "personas a la lejanía que no distingo."

    "Mi cuerpo se levanta ahora caminando hacia ellos pero por más que camino no logro acortar la distancia que tengo con ellos."

    menu:
        "¡¿Quiénes son?!":
            a "¡¿Quiénes son?!"

        "¡¿Dónde están?!":
            a "¡¿Dónde están?!"

        "¡AYUDA!":
            a "¡AYUDA!"

    "Aquellas siluetas voltean a mí, ojos blancos por completo, mi cuerpo se siente nervioso."

    a "¡Díganme algo!"

    "{color=#ffffff}???{/color}" "𒈓𒈙꧅𒈙𒈙"

    "Son palabras que no puedo distinguir, un lenguaje extraño que ya había escuchado en el pasado."

    stop music fadeout 0.5

    #bg salonclases

    scene bg salonclases3 with Fade(1.0, 1.0, 1.0)

    "Abrí mis ojos lentamente acostumbrándome la luz, puedo escuchar las voces de mis compañeros a la lejanía como pequeños ecos."

    "Pronto las memorias regresan: "

    extend "cuando salimos de la biblioteca mi cuerpo se paralizó una vez más, Felix tomó la gorra de mi sudadera y me arrastró lejos hasta llegar al salón."

    "Sí, me acordaba de lo que había ocurrido, como mi cuerpo había dejado de reaccionar por el miedo al igual que a Freya gritando que Evan la soltase."

    #show freya

    fr "¡IDIOTA!"

    scene bg freyacachetadaevan with vpunch

    play sound "sfx/slap.mp3" volume 1.25

    "Se escuchó el fuerte grito de Freya dándole una fuerte cachetada a Evan. Éste inmediatamente caminó hacia atrás y se sostuvo con una mesa comenzando a toser."

    play music "audio/intimate.mp3" volume 0.5

    fr "¡CÓMO TE ATREVES! ¡PODÍA SALVARLA! ¡PODÍA... PODÍA RESCATARLA!"

    "El cubrebocas de Evan cayó revelando una horrible cicatriz a lo largo de su boca, se veía vieja, quizás tenía ya mucho tiempo."

    "Alrededor de su mismo rostro tenía varias cicatrices pero ninguna era tan grande como esta, como si un animal lo hubiese atacado."

    scene bg salonclases3 with dissolve

    show evan nmsangre at left 

    show freya angustiadallora2 at right
    
    with dissolve

    "Evan apartó la vista para comenzar a toser, sangre salía de su boca mientras éste tosía."

    e "Ibas a morir también..."

    show freya angustiadahablallora with dissolve

    fr "¡LO HUBIERA PREFERIDO!"

    "Freya lo tomó de la chaqueta con fuerza aunque después se detuvo, quizás fue el rostro herido del chico o la facilidad con la que aquella pudo tomar su cuerpo."

    #hide evan ?

    hide evan with vpunch

    show freya angustiadallora2 at right with dissolve

    "Molesta, únicamente le dio un empujón y fue suficiente para que Evan se tambaleara y cayera entre las mesas."

    "Rápidamente me levanté, reaccionando inmediatamente, mi cuerpo se movió hacia Evan para ayudarlo a levantarse."

    show freya angustiadahablallora3 with dissolve

    fr "Tú... Tú tienes la culpa de todo."

    "Esta vez me estaba apuntando a mí, sus ojos furiosos viéndome con determinación."

    a "¿Y-... yo?"

    fr "Sí, no debimos ir a la biblioteca, yo sabía que iba a ser un error."

    fr "¡¿Y qué fue lo que lograste?! "
    
    #cambia expresion

    show freya angustiadahablallora with vpunch

    extend "¡NADA!"

    show freya angustiadallora2 at center with move

    "Su cuerpo se movió hacia mí, su puño cerrado hasta alzarse con la intención de golpearme pero se detuvo antes de llegar."

    fr "¡Ustedes, son unos idiotas! Mataron a mi amiga, ustedes... ustedes dejaron que muriera..."

    show freya ladollora with dissolve

    #hide freya

    "La chica se dio la vuelta dándole un fuerte empujón a una mesa conteniendo sus lágrimas moviéndose a una esquina del salón."

    hide freya with dissolve

    #show evan

    a "¿Estás bien?"

    "Esta vez voltee a ver a Evan."

    show evan nmmanosboca at center with dissolve

    e "Sí..."

    "Sabía que mentía, pero tampoco quise presionarlo."

    show evan nmlastimadosangre with dissolve

    "Mis manos buscaron entre mis bolsillos algo que pudiera usar para cubrirse."

    e "Déjalo así..."

    menu:
        "Estás herido, necesitas ayuda":
            a "Estás herido, necesitas ayuda."

        "Pero quiero ayudar":
            a "Pero quiero ayudar."
        
        "No puedo dejarlo así":
            a "No puedo dejarlo así."

    e "Estoy bien..."

    stop music fadeout 0.5
    
    "Un poco asustado asentí con la cabeza dándome la vuelta, no sin antes recibir un pequeño \"gracias\" de la boca de Evan."

    hide evan with dissolve

    #hide evan

    #show felix

    "Caminé a Felix el cual sostenía los libros entre sus manos."

    show felix manofrentepreocupado at center with dissolve

    f "Fue-... Fueron los que pude agarrar, el último se quedó en la biblioteca."

    "Felix los extendió para ofrecerlos."

    "Los examiné lentamente, algo se sentía raro. No sé qué era, pero era algo raro."

    if talk_hanna:
        "El libro era distinto, este era uno que Hanna me había enseñado cuando platicamos."
        
        "La portada era la misma pero al momento de abrirlo el contenido cambiaba, ya no estaba la imagen del monstruo en ninguna de las páginas y tampoco los símbolos que antes había visto."

        "¿Quizás los libros cambiaban su contenido después de un tiempo?"
    else:
        "Por más que los observaba una vibra muy extraña salía de los libros, se sentían oscuros, causaban que un escalofrío recorriera por mi espalda baja por la sensación."

    show felix normal with dissolve

    f "¿Descubriste algo?"

    a "No, nada, no entiendo ninguna palabra."

    f "Bueno, era de esperarse, todos los libros dentro de la biblioteca estaban así, dudo mucho que Hanna haya encontrado algo de valor."

    "Tragué frío, la saliva de mi boca se deslizó como hielo por mi garganta causando nerviosismo en mi interior se intensificara por las palabras de Felix."

    a "No creo que sea así."

    "Intenté mentirme a mí mismo..."

    "¿Y si realmente Hanna no había encontrado algo? "
    
    extend "¿Acaso su muerte había sido en vano?"

    "No"
    
    extend ", no tenía sentido."

    "Mis ojos pasaron por las páginas de los libros "
    
    extend "¿alguna señal? "
    
    extend "¿Hay algo que Hanna haya dejado?"
    
    "Nada, absolutamente nada."

    "Sentí como mis ojos se llenaban de lágrimas por la impotencia, no quería asumir que su muerte había sido para nada."

    show felix pensando with dissolve

    f "Bueno, si no son de utilidad deberíamos dejarlos, solo nos estorbaran si tenemos que correr."

    a "Sí... supongo que tienes razón."

    #hide felix

    hide felix with dissolve

    #bg salon clases

    label cap3true_sideselection:
        scene bg salonclases3 with Fade(0.3, 0.1, 0.3)

        "Dejando los libros de lado, no sin antes darles una última ojeada, un suspiro salió de mi interior."

        "El salón se quedó completamente en silencio a salvo de un par de tosidos de parte de Evan el cual ya traía su cubrebocas puesto nuevamente."

        "Felix estaba recostado sobre la puerta viendo de vez en cuando por la ventana para comprobar que el monstruo no viniese."

        "Freya estaba del otro lado de la habitación de brazos cruzados viendo a algún punto vacío de la habitación."

        $ freya_cap3_talk = False

        menu:
            "Cuidar de Evan":
                call cap3true_evan from _call_cap3true_evan

            "Hablar con Freya":
                call cap3true_freya from _call_cap3true_freya

            "Acompañar a Felix":
                call cap3true_felix from _call_cap3true_felix

    #bg salonclases

    scene bg salonclases3 with Fade(0.3, 0.1, 0.3)

    play music "audio/longtwilight.mp3" volume 0.25

    #show evan

    show evan normal at center

    #show freya

    show freya lado at left

    #show felix

    show felix normal at right

    with dissolve

    "Caminé al centro de la habitación, los demás parecieron juntarse intuitivamente."

    "¿Acaso me había convertido en una especie de líder?"

    "No quería eso, suelo tomar pésimas decisiones, no deberían de estarme siguiendo en absoluto."

    show evan ceja with dissolve

    e "¿Y ahora qué?"

    "Evan preguntó, Freya pareció ignorarlo."

    a "Amm, bueno, la verdad no lo sé."

    "Mi esperanza era lo que estaba en la biblioteca pero solo había acabado con un par de libros inútiles y una ilustración de Loki."

    show freya ladohabla2 with dissolve

    fr "Quizás podríamos ir a la oficina del director, es otra biblioteca ahí dentro."

    show evan gimme with dissolve

    e "Pero eso está en el segundo piso."

    fr "Puedes quedarte aquí si quieres."
    
    a "No, hay que permanecer unidos."

    show felix pensando2 with dissolve 

    f "¿Y eso a que nos ha llevado? Quizás deberíamos separarnos."

    if freya_cap3_talk:
        show freya normalhabla with dissolve

        fr "No, estoy de acuerdo con Arden."

        fr "Es más probable que podamos ayudarnos a escapar estando juntos que si nos separamos. "

        show freya pensarhabla with dissolve
        
        extend "Además, como ya había dicho, ninguna película de terror acaba bien si nos separamos."
    else:
        show freya normalhabla with dissolve

        fr "No, estoy de acuerdo con..."

        show freya caderaspreocupada2 with dissolve

        "Hizo una pausa y volteo una vez más hacia mí, aunque esta vez lo miraba pidiendo perdón."

        a "Arden."

        show freya normal with dissolve

        fr "Arden."
        
        fr "Es más probable que podamos ayudarnos a escapar estando juntos que si nos separamos. "

        show freya pensarhabla with dissolve
        
        extend "Además, como ya había dicho, ninguna película de terror acaba bien si nos separamos."

    "Tomando esto en cuenta quizás esa era la razón por la cual Hanna murió, se separó del grupo. Era más seguro ir unidos."

    show evan ladobrazoenojado with dissolve

    e "Tsk, no iré."

    "Evan declaró dándose la vuelta y caminando a la entrada."

    a "¿A dónde vas?"

    show evan ladobrazo with dissolve

    e "No lo sé, lejos."

    #hide evan

    hide evan with dissolve

    "Evan salió del salón sin decir nada más."

    show freya lado with dissolve

    "Mis ojos voltearon a Freya quien se encogió de hombros como si no le importase del todo Evan, aunque, no pudo disimular que dio un paso para seguirlo."

    show felix manofrenteceja with dissolve

    f "Bueno, entonces... ¿a la oficina del rector?"

    "Freya y yo asentimos con la cabeza"

    stop music fadeout 0.5
    
    "Fue cuando Evan volvió a entrar cerrando la puerta del salón"

    play sound "sfx/1doorbang.mp3" volume 0.75

    #show evan

    show evan despair at center with dissolve

    extend ", sus ojos palpitaban terror y se notaba preocupado."

    e "Estamos jodidos."

    "Evan comenzó a toser, se llevó su antebrazo a su boca para cubrirse."

    show freya angustiadahabla with dissolve

    fr "¿Qué?"

    show evan gimmeenojado with vpunch

    play music "audio/beast1.mp3" volume 0.25

    e "¡¡Estamos jodidos!!"

    a "¿A qué te refieres?"

    e "Afuera, hay un humo, es tóxico. Lo conozco, tiene propiedades que investigamos una vez en clase."

    show freya caderaspreocupada2 with dissolve

    fr "Tsk, ¿cómo sabemos que no nos engañas?"

    show evan ladobrazoenojado with dissolve

    e "¡¿POR QUÉ LOS ENGAÑARÍA?!"

    show freya apunta with dissolve

    fr "¡Porque literalmente hace unos minutos no querías nada que ver con nosotros!"

    show evan ladobrazo with dissolve

    e "Claro, no es como que quiera volver a verte."

    fr "¿Huh? ¿Eso qué tiene que ver?"

    "Freya se acercó a él quitándolo de la puerta de un tirón. Ésta vio el humo desde la ventanilla de la puerta y luego se volteó a Evan de forma incrédula."

    show evan normal with dissolve

    e "Adelante, no pienso detenerte."

    #hide freya

    hide freya with dissolve

    "La chica salió rápidamente cerrando la puerta detrás de ella"
    
    #show freya

    show freya preocupada at left with dissolve

    play sound "sfx/1doorbang.mp3" volume 0.75

    extend ", luego de unos segundos regresó."

    fr "Mierda... Estamos atrapados."

    a "¿A...atrapados?"

    show freya angustiada with dissolve

    fr "Las puertas del pasillo también están cerradas... no podemos salir de aquí... ¿En cuánto tiempo hace efecto el humo?"

    show evan pensando with dissolve

    e "Quizás en ustedes unos 7 minutos para perder la conciencia, bueno, en el hipotético caso de que el salón esté lleno del humo, mientras tengamos oxígeno tenemos más tiempo."

    show evan despair with dissolve

    e "Yo, sin embargo, en 2 minutos estoy muerto..."

    show freya angustiadahabla with dissolve

    fr "¡CALLA! ¡No dejaré que nadie más muera, ni siquiera tú! Hay que checar las rutas de evacuación."

    #maybe un bg que tenga el salon con humo, o un overlay de humo.

    show humoverde zorder 2 with dissolve

    "El humo comenzó a meterse lentamente debajo de la puerta cubriendo un poco los pies de todos."

    show freya caderaspreocupada2 with dissolve

    fr "¡Mierda, mierda!"

    show felix manofrentepreocupadohabla2 with dissolve

    f "La ruta de escape está bloqueada, Freya."

    show freya angustiadahabla with dissolve

    fr "¡Debe de haber algo, alguna forma!"

    "La ansiedad ahora me empezaba a consumir: "
    
    extend "vas a morir, vas a morir, todos aquí van a morir."

    a "¡No quiero, no quiero, no quiero!"

    show freya angustiadahabla with vpunch

    a "¡¡NO QUIERO MORIR!!"

    play sound "sfx/doorbang.mp3" volume 0.75

    "Comencé a caminar hacia la salida desesperado y golpeé las ventanas con fuerza buscando romperlas."

    fr "¡ESPERA, NO! ¡Vas a alertar al monstruo!"

    a "Me voy a morir de todas formas."
    
    #un vpunch o algo chido, idk

    show bg salonclases3 with vpunch

    extend " ¡NOS VAMOS A MORIR FREYA!"

    show freya preocupada with dissolve

    fr "Tranquilo, vamos a salir de esta."

    show freya normal with dissolve

    fr "Hay que encontrar la salida."

    #hide evan, felix

    hide evan

    hide felix

    with dissolve

    "Los otros dos asintieron con la cabeza y comenzaron a buscar entre los casilleros y cajones algo de utilidad."

    #hide freya

    hide freya with dissolve

    stop music fadeout 1.5

    "Sea lo que sea que dijeran, yo ya no los estaba escuchando"
    
    extend ", no"
    
    extend ", mis pensamientos estaban destrozados"

    play sound "sfx/heartbeat.mp3" loop volume 0.5
    
    extend ", tengo miedo"
    
    extend ", mucho miedo."

    "Mi cuerpo se deslizó sobre la pared hasta quedar en el suelo, el humo pesado invadiendo poco a poco mis pulmones mientras el pánico estaba llenándome."

    scene bg black with dissolve

    "No quiero morir"
    
    extend ", no quiero morir"
    
    extend ", por favor, no quiero morir." 
    
    "Era lo único que se repetía varias veces en mi cabeza."
    
    "No quiero morir, no quiero morir."

    "Mi desesperación aumentaba mientras las lágrimas caían recorriendo mis mejillas."
    
    "...Por favor..."
    
    extend "alguien, sálveme, por favor."

    menu:
        "Darse por vencido.":
            jump cap3true_badend1

        "No darse por vencido.":
            stop sound

            "{color=#435f21}???{/color}" "No te rindas"

    a "¿Katherine?"

    "{color=#435f21}???{/color}" "Yo sé, yo sé que tú eres mejor que esto."

    a "¡KATHERINE!"

    #vpunch probs

    play sound "sfx/1doorbang.mp3" volume 0.75

    show bg salonclases3 
    
    show humoverde zorder 2
    
    with vpunch

    "Alcé la cabeza rápidamente golpeándome contra la mesa y, como si fuese un milagro, un sobre cayó sobre mis piernas."

    "Estaba debajo de una mesa después de todo y el movimiento pareció haber despegado el sobre que estaba atado a la misma."

    "Tomé el sobre y lo abrí"
    
    #bg pista binario

    play music "audio/clue.mp3" volume 0.25

    scene bg pistabinario with dissolve

    pause 1.0
    
    extend ", era un código, un código binario, y hasta abajo un C3."

    scene bg pistabinario with Dissolve(2.0)

    #bg salon con humoa

    scene bg salonclases3
    
    show humoverde zorder 2

    with dissolve

    #vpunch

    show bg salonclases3 with vpunch

    a "¡¡AHH!!"

    "Me levante con rapidez, golpeando mi cabeza."

    #show freya

    #show evan

    show freya angustiadahabla at left

    show evan gimmeenojado at right

    with dissolve

    fr "HEY."

    e "¡Arden!"

    "Ambos estaban cerca, parecía que estaban gritando desde antes o quizás discutiendo como es de costumbre."

    a "¡Encontré algo!"

    #show felix

    show felix normal at center with dissolve

    f "¿Qué es?"

    a "Un sobre... debe traer algo que nos ayude, ¿no?"

    show evan pensando with dissolve

    e "Código binario. "

    show evan normal with dissolve
    
    extend "¿Alguien aquí sabe leer... código binario?"

    "Todos negaron con la cabeza."

    a "Ah, estudie un poco, por... Historia de la literatura. Pero, no recuerdo todos los números..."

    "Tomando una pluma de mi bolsillo, anoté los números que conocía en la parte de atrás del sobre."

    a "Tendremos que adivinar el resto..."

    show evan gimmeceja with dissolve

    e "Es de cuatro números... aun así, ¿dónde se pone el código?"

    show freya pensarhabla with dissolve

    fr "¿En el C3? Es un casillero, ¿no?"

    "Freya volteó a los casilleros donde estaban ordenados por letras, y solo uno estaba cerrado."

    hide freya

    hide evan

    hide felix

    with dissolve

    "Todos nos acercamos, habían varios números tachados a su alrededor y un par de puntos más."

    #bg binarioypista

    scene bg pistabinario with dissolve

    $ binario_fail_counter = 0

    label cap3true_binario:
        if binario_fail_counter > 5:
            jump cap3true_binario_fail

        $ codigo_input = int(renpy.input("Introduce el código:", "", allow="0123456789", length=4))

        if codigo_input != codigo_real:
            fr "No tenemos mucho tiempo, Arden. Concéntrate por favor."

            $ binario_fail_counter += 1

            jump cap3true_binario

    #bg salonclases humo

    show bg salonclases3
    
    show humoverde zorder 2

    with Fade(0.3, 0.1, 0.3)

    "Finalmente se abrió la puerta y ahí había otra ilustración doblada."

    a "Otra imagen..."

    "La desdoble para ver lo que tenía dentro. "
    
    #bg pistaolimpo

    scene bg black with Fade(0.3, 0.1, 0.3)
    
    extend "Era una imagen de una entrada, un cuadrado y líneas de perspectiva."

    a "Huh..."

    fr "La... Es la entrada del Olimpo."

    a "¿Perspectiva?"

    #bg salon de clases humo

    show bg salonclases3
    
    show humoverde zorder 2
    
    with Fade(0.3, 0.1, 0.3)

    #show evan, freya, felix

    "Ladee mi cabeza confundido y Evan se encogió de hombros de la misma forma."

    a "Quizás si lo alineamos..."

    #bg salonalineado

    scene bg salonclases3
    
    show humoverde zorder 2
    
    with Fade(0.3, 0.1, 0.3)

    "Poniéndolo en varias posiciones alrededor de la habitación, finalmente lo alineó con el pizarrón, revelando que la entrada del olimpo quedaba en un cuadro del techo."

    a "Hey... esa pieza..."

    #show freya

    show freya angustiadahabla at center with dissolve

    fr "No perdemos nada, ¡rápido!"

    #hide freya

    "Ella corrió hacia la pieza del techo que apuntaba el olimpo y subiendo a una mesa la removió revelando así un pasadizo entre las ventilaciones, uno lo suficientemente amplio para que todos pudieran pasar."

    #show evan

    show evan gimmeenojado at right with dissolve

    e "¡¿QUÉ ESPERAS?! ¡HAY QUE IRNOS!"

    "Freya asintió con la cabeza y todos comenzamos a subir ayudándonos entre nosotros."

    stop music fadeout 0.5

    #bg ventilacion ?

    scene bg ventilacion with dissolve

    "Ya dentro se escucha cómo el viento sopla con fuerza y recorre aquel lugar frío para mantener ventilados los salones."

    "Entre vueltas y el continuo miedo de la oscuridad, una pequeña luz se empezó a ver a lo lejos, venía de arriba."

    play sound "sfx/metaldoor.wav" volume 0.5

    "Freya, quien guiaba al grupo, abrió la escotilla revelando la oficina del rector."

    jump cap4true

label cap3true_badend1:
    #bg salonconhumo
    
    # show bg salonclases3
    
    # show humoverde zorder 2

    # with fade

    "Lento... mi cuerpo comenzó a sentirse lento, los pulmones que estaban siendo invadidos por el humo hicieron que mi respiración poco a poco se ralentizará."

    "Cansado, mi cuerpo se relajaba cediendo al veneno entrando en trance era como si poco a poco mi mente dejase de pensar."

    "Pensar..."

    #algun blur?

    # scene bg black with dissolve

    "Pensar..."

    "Pensar..."

    "Pensar en lo que había pasado."

    "No, no quiero pensar en eso."

    "No quiero tener miedo."

    "Estoy cansado..."

    "Muy cansado..."

    "..."

    "..."

    #bg badend

    return

label cap3true_binario_fail:
    stop music fadeout 0.5

    show bg salonclases3
    
    show humoverde zorder 2
    
    with Fade(0.3, 0.1, 0.3)

    "Agh..."

    "No pude..."

    "No me podía concentrar..."

    play sound "sfx/1heartbeat.mp3" volume 0.75

    scene bg black with Dissolve(0.25)

    scene bg salonclases3

    show humoverde zorder 2
    
    with Dissolve(0.25)

    "Con cada intento que hacía, mi energía se disipaba."

    play sound "sfx/1heartbeat.mp3" volume 0.75

    scene bg black with Dissolve(0.25)

    scene bg salonclases3

    show humoverde zorder 2
    
    with Dissolve(0.25)

    "No..."

    "No puedo..."

    play sound "sfx/fall.ogg" volume 0.5

    show bg salonclases3 with vpunch

    "Escuché el impacto de Evan cayendo al suelo."

    fr "¡Ahh, Evan!"

    play sound "sfx/1heartbeat.mp3" volume 0.75

    scene bg black with Dissolve(0.25)

    scene bg salonclases3

    show humoverde zorder 2
    
    with Dissolve(0.25)

    "Pero no pude voltear."

    play sound "sfx/1heartbeat.mp3" volume 0.75

    scene bg black with Dissolve(0.25)

    scene bg salonclases3

    show humoverde zorder 2
    
    with Dissolve(0.25)

    "Me estoy quedando sin energía..."

    play sound "sfx/1heartbeat.mp3" volume 0.75

    scene bg black with Dissolve(0.25)

    scene bg salonclases3

    show humoverde zorder 2
    
    with Dissolve(0.25)

    play sound "sfx/1heartbeat.mp3" volume 0.75

    scene bg black with Dissolve(0.25)

    scene bg salonclases3

    show humoverde zorder 2
    
    with Dissolve(0.25)

    play sound "sfx/1heartbeat.mp3" volume 0.75

    scene bg black with Dissolve(0.5)

    "..."

    "Supongo que... "

    extend "este es el final..."

    "..."

    "..."

    "..."

    return
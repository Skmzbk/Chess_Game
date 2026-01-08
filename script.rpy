# Coloca el código de tu juego en este archivo.

#region Definiciones de Personajes y Variables
# Declara los personajes usados en el juego como en el ejemplo:

define i = Character("Isaac", color="#e3c6c5")
define m = Character("Monstruo", color="#c9192a")
define e = Character("")
define depth = 1
default score = 0
default chess_return_label = None  # Label al que volver después de perder
default victoria = False
default empate = False

# Definiciones de imágenes de personajes
image isaac = "Isaac.PNG"
image monstruo = "Monstruo.PNG"
image monstruo2 = "Monstruo2.PNG"
image monstruo3 = "Monstruo3.PNG"
image monstruo4 = "Monstruo4.PNG"

# Definiciones de escenas de fondo
image titulo_nivel_1 = "images/Backgrounds/Titulos/titulo_nivel_1.PNG"
image bg_nivel_1 = "images/Backgrounds/Bgs/bg_nivel_1.png"
image titulo_nivel_2 = "images/Backgrounds/Titulos/titulo_nivel_2.PNG"
image bg_nivel_2 = "images/Backgrounds/Bgs/bg_nivel_2.png"
image titulo_nivel_3 = "images/Backgrounds/Titulos/titulo_nivel_3.PNG"
image bg_nivel_3_1 = "images/Backgrounds/Bgs/bg_nivel_3_1.png"
image bg_nivel_3_2 = "images/Backgrounds/Bgs/bg_nivel_3_2.png"
image bg_nivel_3_3 = "images/Backgrounds/Bgs/bg_nivel_3_3.png"
image bg_nivel_3_4 = "images/Backgrounds/Bgs/bg_nivel_3_4.png"
image titulo_nivel_4 = "images/Backgrounds/Titulos/titulo_nivel_4.PNG"
image bg_nivel_4_1 = "images/Backgrounds/Bgs/bg_nivel_4_1.png"
image bg_nivel_4_2 = "images/Backgrounds/Bgs/bg_nivel_4_2.png"
image game_over = "images/Backgrounds/Titulos/game_over.PNG"

# Definiciones de endings (si no existen estas imágenes, se usarán placeholders)
# TODO: Crear estas imágenes o reemplazar con las imágenes reales
image ending_good = "black"  # Placeholder - reemplazar con imagen real
image ending_bad = "black"   # Placeholder - reemplazar con imagen real
image ending_fanon = "black" # Placeholder - reemplazar con imagen real
#endregion

#region Animaciones de Fondo
# Definiciones de animaciones de fondo (2 frames cada una)
# Formato: anim_## donde ## es el número de animación
image anim_11:
    "images/Backgrounds/Intro/11.PNG"
    0.5
    "images/Backgrounds/Intro/12.PNG"
    0.5
    repeat

image anim_21:
    "images/Backgrounds/Intro/21.PNG"
    0.5
    "images/Backgrounds/Intro/22.PNG"
    0.5
    repeat

image anim_31:
    "images/Backgrounds/Intro/31.PNG"
    0.5
    "images/Backgrounds/Intro/32.PNG"
    0.5
    repeat

image anim_41:
    "images/Backgrounds/Intro/41.PNG"
    0.5
    "images/Backgrounds/Intro/42.PNG"
    0.5
    repeat

image anim_51:
    "images/Backgrounds/Intro/51.PNG"
    0.5
    "images/Backgrounds/Intro/52.PNG"
    0.5
    repeat

image anim_61:
    "images/Backgrounds/Intro/61.PNG"
    0.5
    "images/Backgrounds/Intro/62.PNG"
    0.5
    repeat

image anim_71:
    "images/Backgrounds/Intro/71.PNG"
    0.5
    "images/Backgrounds/Intro/72.PNG"
    0.5
    repeat

image anim_81:
    "images/Backgrounds/Intro/81.PNG"
    0.5
    "images/Backgrounds/Intro/82.PNG"
    0.5
    repeat

image anim_91:
    "images/Backgrounds/Intro/91.PNG"
    0.5
    "images/Backgrounds/Intro/92.PNG"
    0.5
    repeat

image anim_101:
    "images/Backgrounds/Intro/101.PNG"
    0.5
    "images/Backgrounds/Intro/102.PNG"
    0.5
    repeat

image anim_111:
    "images/Backgrounds/Intro/111.PNG"
    0.5
    "images/Backgrounds/Intro/112.PNG"
    0.5
    repeat

image anim_121:
    "images/Backgrounds/Intro/121.PNG"
    0.5
    "images/Backgrounds/Intro/122.PNG"
    0.5
    repeat

image anim_131:
    "images/Backgrounds/Intro/131.PNG"
    0.5
    "images/Backgrounds/Intro/132.PNG"
    0.5
    repeat
#endregion

# THIS_PATH is defined in chess_displayable.rpy
# define THIS_PATH = '00-chess-engine/'
init python:
    # for importing libraries
    import_dir = os.path.join(renpy.config.gamedir, THIS_PATH, 'python-packages')
    # to prevent STOCKFISH_ENGINE from getting stored and pickled
    global_objects = {}

# El juego comienza aquí.

#region labels
label start:

    # Botones para saltar labels (solo para propositos de testeo)
    screen test_jump_menu():
        frame:
            align (0.98, 0.02)
            background "#222c"
            vbox spacing 6:
                text "JUMP TO:" color "#fff" size 18
                textbutton "Inicio" action Jump("start")
                textbutton "Primer Nivel" action Jump("primer_nivel")
                textbutton "Segundo Nivel" action Jump("segundo_nivel")
                textbutton "Tercer Nivel" action Jump("tercer_nivel")
                textbutton "Cuarto Nivel" action Jump("cuarto_nivel")
                textbutton "Epilogo" action Jump("epilogo")
    if config.developer:
        show screen test_jump_menu

    # Muestra una imagen de fondo: Aquí se usa un marcador de posición por
    # defecto. Es posible añadir un archivo en el directorio 'images' con el
    # nombre "bg room.png" or "bg room.jpg" para que se muestre aquí.

    # Muestra un personaje: Se usa un marcador de posición. Es posible
    # reemplazarlo añadiendo un archivo llamado "eileen happy.png" al directorio
    # 'images'.

    # Presenta las líneas del diálogo.
    play music "music/Waltz - Tschikovsky Op. 40.mp3" fadeout 1.0
    scene anim_11
    "Isaac encontró un polvoriento juego de ajedrez en un rincón de la casa, junto a un viejo libro de estrategias."
    scene anim_21
    "Como su madre le había quitado casi todas sus pertenencias, aquello era lo único que tenía para entretenerse."
    scene anim_31
    "Lo que nunca imaginó es que llegaría a obsesionarse con ese descubrimiento."
    scene anim_41
    "Día y noche hojeaba el libro, aprendía nuevas técnicas y resolvía cada problema que encontraba."
    scene anim_51
    "Su obsesión creció tanto que comenzó a soñar partidas contra Kasparov, Carlsen, Capablanca y Fischer. Su pequeña mente se llenó de torres, caballos y sacrificios brillantes."
    scene anim_61
    "Una tarde, mientras Isaac jugaba una partida imaginaria con Guppy..."
    scene anim_71
    "su madre entró en la habitación."
    scene anim_81
    "Al ver el tablero, se lo arrebató sin decir una palabra. Aseguró que ese \"juego corrupto\" lo estaba desviando del camino correcto."
    scene anim_91
    "Como castigo por su “mal comportamiento”, lo encerró en el armario."
    scene anim_101
    "Isaac, triste y sollozando, se dejó caer en el suelo."
    scene anim_111
    "Pero entre sus lágrimas notó algo extraño: una débil luz filtrándose desde el fondo del armario. Curioso, se arrastró hacia ella… y, entre aquel brillo centellante y la oscuridad más profunda..."
    scene black
    "Perdió el equilibrio y cayó."
    scene anim_121
    "Cuando abrió los ojos, se hallaba en un calabozo apenas iluminado."
    "Su miedo casi lo paraliza, hasta que ve algo que lo desconcierta… y lo tranquiliza al mismo tiempo..."
    scene anim_131
    "Un ajedrez gigante... Y detrás del tablero… un horripilante monstruo."

label primer_nivel:

    stop music
    scene titulo_nivel_1
    play sound "sounds/Long Suspense 2.mp3" fadeout 1.0
    "Capitulo uno"
    scene bg_nivel_1
    play music "music/H/This House.mp3" fadeout 1.0
    "Isaac se acerca al tablero con mucho temor y ansiedad pero curioso"
    show isaac at left
    i "Ah… uh… ahh…"
    show monstruo at right
    m "Hablas raro, niño. Pero… por alguna razón puedo entenderte."
    "El monstruo avanza unos pasos, su sombra envolviendo el tablero."
    m "Este es el Calabozo del Ajedrez. Fue sellado hace siglos dentro de un tablero y un libro polvoriento… sí, justo los que encontraste."
    m "Alguien debía retirarlos de su sitio. En el momento que tu madre los tomó… despertamos. Y ahora podemos subir a la superficie."
    m "Pero como toda historia basada en un juego, el mismo juego tiene el poder de volver a sellarnos."
    "El monstruo ríe, un sonido húmedo y vibrante que retumba en las paredes."
    m "Por fortuna, hemos tenido muchísimos años para practicar. Por ridícula que sea nuestra debilidad, nadie podrá detenernos."
    i "Uh… ahh… eh… ihh… ahhh…"
    m "¿Qué dices? ¿Que tú puedes detenernos?"
    i "Asiente tembloroso."
    m "¿En serio hablas en serio?"
    "El monstruo se acomoda detrás del enorme tablero."
    m "Bueno… no pierdo nada calentando un poco antes de sembrar el terror allá arriba. Y tampoco tengo muchas opciones, ¿verdad?"
    "El tablero se ilumina."
    "Comienza la partida."
    
    # Establecer el identificador para saber a dónde volver si pierde
    $ chess_return_label = "primer_nivel"
    
    call chess_game from _call_chess_game

    if victoria:

        $ victoria = False
        hide monstruo
        e "Milagrosa victoria, Isaac vence al primer monstruo el cual yace tirado en el suelo inherte"
        e "Isaac no puede volver pues no hay manera asi que lo unico que le queda es avanzar y esperar lo mejor..."        

    elif empate:

        $ empate = False
        play music "music/F/Goblin_Tinker_Soldier_Spy.mp3" fadeout 1.0
        m "Bueno esto es una sorpresa, las \"leyes del ajedrez\" me impiden hacerte algo asi que lo mejor sera que pases con mi supervisor"
        i "ahh ehh uhhh"
        m "Lo se, lo se es raro pero no estoy preparado para estas situaciones sigue adelante y te atiende a la brevedad"
        e "Isaac avanza un poco confundido y nervioso pero sin opcion"

    else:

        return

label segundo_nivel:

    stop music
    scene titulo_nivel_2
    play sound "sounds/Long Suspense 2.mp3"
    "Capitulo dos"
    scene bg_nivel_2
    play music "music/H/Hush.mp3" fadeout 1.0
    # ---------- NIVEL 2 ----------

    e "Isaac seguía completamente confundido por lo que acababa de ocurrir."
    e "Aquel lugar era aterrador, extraño, y no había forma de volver por donde había caído."
    e "Y lo del monstruo anterior... había sido totalmente inesperado."

    e "Pero no tenía otra opción más que seguir avanzando."

    e "Caminó y caminó por un largo pasillo. Estaba cansado, pero curiosamente se sentía menos aterrado que en su casa..."
    e "Al menos aquí nadie le gritaba. Nadie le decía que no era suficiente."

    show monstruo2 at right

    "*CRACK*"

    show isaac at left

    i "¡Ahhhhh!"

    e "De la nada, justo frente a él, apareció un monstruo de aspecto grotesco e imponente."


    # ---------- RUTA SCORE = 0 (humor) ----------

    if score == 0:

        play music "music/F/Krampus Workshop.mp3" fadeout 1.0
        m "Buenas tardes, caballe… rito… emm… esto es un poco incómodo."
        i "Ahhh… uhh… ehhh…"

        m "Sí, sí, ya me comentó mi compañero que empató contigo en la partida pasada."
        m "Lo cual es rarísimo, por cierto, pero bueno…"

        m "A ver, déjame ver… por aquí tengo el documento correspondiente."
        m "\"Manual de procedimientos para aniquilar niños que saben mucho de ajedrez y podrían acabar con los planes malvados de monstruos sellados en una cueva por el ajedrez\"."

        m "Sí, el título es larguísimo. Pero como era una situación bastante específica y nadie pensó que pasaría… pues decidieron ser igual de específicos."

        m "Veamos qué toca hacer…"

        m "…"
        m "…"
        m "…"

        m "Ajá, aquí está."
        m "\"Gánale al infante en ajedrez. Por dios, ¿no sabes de qué trata el juego?\""

        m "Bueno, no encuentro fallas en esa lógica."
        m "Prepárate, niño."

        i "Uhh… ahhh… ehhh…"


    # ---------- RUTA SCORE = 1 (terror) ----------

    else:

        m "Grrrrrrrr…"

        i "…"

        e "Isaac quedó paralizado ante la presencia de aquella aberración."
        e "Los ojos del monstruo estaban clavados en él, inmóviles, como si diseccionaran cada fibra de su ser."

        e "Isaac quería gritar con todas sus fuerzas… pero su cuerpo no le respondía."
        e "Su garganta se tensó. El aire se aferró a su abdomen, negándose a salir."
        e "Era incapaz de emitir siquiera un susurro."

        e "De repente, el monstruo retrocedió lentamente, colocándose frente a un enorme tablero de ajedrez."

        e "Allí se detuvo. Quedó completamente inmóvil, como una estatua."
        e "No respiraba. No emitía sonido. No había latido alguno."

        e "Aun así, su presencia bloqueaba por completo el puente que seguía más adelante."

        e "La mesa, corroída y torcida, mostraba con claridad lo inevitable:"
        e "La única manera de avanzar… era ganar otra partida."


    $ chess_return_label = "segundo_nivel"
    call chess_game from _call_chess_game_1

    if victoria:

        play music "music/H/Hush.mp3" fadeout 1.0
        $ victoria = False

        e "En cuanto Isaac movió la pieza que daba jaque mate, un sonido retumbó dentro del monstruo."
        e "Era como si un animal hubiese sido despertado y arañara desde adentro."

        e "El cuerpo del monstruo comenzó a tambalearse violentamente, como si hiciera un berrinche."
        e "Lo que antes parecía una estatua inmóvil empezó a contorsionarse como un ser vivo."

        e "Respiraba rápido. Todo su cuerpo palpitaba como si una sangre espesa fuera forzada a circular."

        e "Isaac, aún en alerta por el estrés de la partida, reaccionó al instante."
        e "Aprovechó los movimientos erráticos del monstruo para correr hacia el puente."

        e "El puente era viejo, inestable, y se agitaba peligrosamente bajo sus pies."
        e "Isaac corría con todas sus fuerzas, intentando escapar lo más rápido posible."

        e "Al voltear, vio al monstruo explotar de manera violenta."
        e "Restos de su cuerpo salieron disparados en todas direcciones, iluminados apenas por la tenue luz del calabozo."

        e "La explosión hizo colapsar la entrada del puente."

        e "Isaac estaba cerca del final, así que siguió corriendo sin detenerse."

        e "En el último instante, saltó…"

        e "…pero su impulso no fue suficiente."

        e "Isaac cayó junto con el resto del puente, descendiendo hacia un abismo tan profundo que su final no podía verse."

        
    elif empate:
        
        play music "music/F/Krampus Workshop.mp3" fadeout 1.0
        $ empate = False

        scene elevador

        m "Uuuf… empate. Eres bueno, niño, pero no lo suficiente."
        m "Aunque… debo admitir que me estoy poniendo un poco nervioso."

        i "Ihh… ahh… uhhh… ehhhh…"

        m "Sí, sí, no me lo tienes que decir. Este procedimiento no estaba en el manual."
        m "De acuerdo, haremos esto, porque de verdad ya me estás metiendo en una situación complicada."

        m "Vas a caminar por este pasillo y al fondo, a la derecha, encontrarás un elevador."
        m "Ese te llevará a \"Super Gerencia\". Mi supervisor sabrá qué hacer contigo."

        i "Ihh… ehh… uhhh… ahhhh…"

        m "Ah, el puente. Sí, olvídate de él."
        m "En realidad es una trampa. Del otro lado no hay nada."
        m "El objetivo es usarlo para atrapar enemigos… o gente que no sabe jugar ajedrez."
        m "De hecho no es nada seguro, necesita mantenimiento. Podría caerse en cualquier momento."

        i "Ehhh…"

        m "Ni lo menciones. Te diría \"cuídate\", pero eres nuestro enemigo."
        m "Así que… no te cuides."

        i "Mhp."


    else:

        return

label tercer_nivel:
    
    stop music
    play sound "sounds/Long Suspense 2.mp3"
    scene titulo_nivel_3
    "Capitulo tres"
    scene bg_nivel_3_1
    play music "music/H/Symmetry.mp3"
    e "Isaac se encontraba en una habitación gigantesca y completamente blanca."
    e "Frente a él había un set de piezas negras de ajedrez, colosales y conscientes."

    scene bg_nivel_3_2

    e "Todas lo miraban desde arriba… con desprecio."


    "Peon" "Mírenlo. Le cuesta tanto ganar… como si fuera difícil."
    i "…"

    "Caballo" "Me sorprende que siga jugando, si todos sabemos que eventualmente va a perder."
    i "…"

    "Alfil" "Así es. Si se rindiera nos ahorraría tiempo… y a él, la vergüenza."
    i "…"

    "Torre" "Qué vergüenza ser sus piezas."
    i "…"

    "Reina" "¿Cuántas veces no te has equivocado, Isaac? ¿Cuántas piezas has regalado?"
    i "…"

    "Rey" "…"

    scene black

    e "…"
    e "…"
    e "Isaac despierta en una oscuridad absoluta."
    e "Lo único que recuerda es caer… caer durante tanto tiempo que se quedó dormido."

    e "Se levanta lentamente, sin ver nada a su alrededor."
    e "Gatea en la oscuridad hasta tocar una pared, y comienza a caminar siguiendo su superficie."

    e "Pasan varios minutos así, hasta que un tenue destello morado aparece a lo lejos."
    e "El corazón de Isaac se acelera. Por primera vez en mucho tiempo… siente esperanza."

    e "Avanza lo más rápido que la oscuridad le permite."

    e "Y entonces choca contra algo gelatinoso que lo absorbe al instante."

    scene bg_nivel_3_3

    e "Frente a él, un ser horripilante se ilumina agresivamente."
    show monstruo3 at right
    e "Patrones morados brillan sobre su cuerpo deforme, como restos radioactivos."
    e "Miles de ojos—pequeños, como huevecillos de pez—lo observan con una intensidad insoportable."

    e "Isaac está paralizado en la masa gelatinosa."
    e "Pero al mirar alrededor, ve una mesa de ajedrez."

    e "Y sabe perfectamente qué viene ahora."
    

    if score < 2:

        play music "music/F/Sergio's Magic Dustbin.mp3"
        m "Saludos, mi enigmático amigo."
        m "Bienvenido a mi humilde morada. Disculpa lo gelatinoso… lo necesito para vivir."
        m "Y para mantener hidratados mis preciosos ojos."

        m "Pero no te dejes engañar por mi tono amable."
        m "Nadie aquí tiene tantas ganas de deshacerse de ti como yo."

        m "Veamos…"
        m "En el expediente que me entregó mi secretaria—trabaja rapidísimo, por cierto, merece un ascenso—"
        m "Dice que no has perdido contra ninguno de mis dos subordinados."

        m "¿Sabes qué significa eso, niño?"
        m "Que nos haces quedar muy mal."

        m "Esta compañía se toma MUY en serio el exterminio y la aniquilación."
        m "Así que, de la manera más atenta posible, te voy a pedir… que pierdas."

        m "Por favor."

        m "Bueno. Comencemos."



    else:
        
        e "Antes de hacer la primera jugada, Isaac siente que pierde energía."
        e "Una especie de terminación nerviosa del monstruo se le ha clavado en el pie."
        e "Cada segundo se hunde más, subiendo por su pierna como una aguja viva."

        show isaac at left
        i "Ahhh!"

        e "La sensación se vuelve insoportable. Siente cómo su cuerpo se debilita."
        e "Isaac comprende que esta partida debe ganarla rápido…"
        e "O no saldrá vivo esta vez."
       

    $ chess_return_label = "tercer_nivel"
    call chess_game from _call_chess_game_2
    

    if victoria:

        play music "music/H/Symmetry.mp3" fadeout 1.0

        $ victoria = False

        e "¡Jaque mate!"
        e "En el instante en que Isaac coloca la pieza final, un fulgor morado estalla desde el tablero."

        e "Las terminaciones nerviosas enterradas en su piel—que ya habían llegado a su cuello,"
        e "poniendo su piel en un tono morado casi negro—"
        e "salen violentamente disparadas de su cuerpo."

        e "La gelatina que lo aprisionaba se desintegra y salpica a su alrededor."

        e "Isaac cae al suelo jadeando."

        e "La tenue luz morada que lo había guiado hasta ese lugar aumenta su intensidad."
        e "Poco a poco revela un paisaje extraño, como un sueño invertido."

        scene bg_nivel_3_4

        e "Isaac se encuentra en una sala larguísima, un pasillo sin fin."
        e "El piso entero tiene un patrón de ajedrez… hasta donde la vista alcanza."


        
    elif empate:

        $ empate = False

        scene bg_nivel_3_4

        play music "music/F/Sergio's Magic Dustbin.mp3" fadeout 1.0

        show monstruo3 at right
        m "Sabes… ahora entiendo por qué tu caso ha sido tan complicado."
        m "De miles de personas, solo unos pocos llegan hasta aquí."
        m "Tienes talento. El suficiente para empatar con horrores inimaginables."
        m "Eso te hace… especial."

        m "Y me encantaría ayudarte más, pero…"
        m "Este no es mi departamento."
        m "Y no me pagan lo suficiente para procesar niños problemáticos."

        m "Así que toma, niño."
        m "Este formulario."

        show isaac at left
        i "Ahh…?"

        m "Llénalo y entrégalo en la siguiente ventanilla."
        m "La sabrás cuando la veas."


        m "Ahora apúrate, este jueguito me atrasó muchísimo."
        m "Tengo montañas de papeleo pendiente."


    else:

        return

label cuarto_nivel:
    
    stop music
    play sound "sounds/Long Suspense 2.mp3"
    scene titulo_nivel_4
    "Capitulo cuatro"

    scene bg_nivel_4_1
    play music "music/H/Giant Wyrm.mp3" fadeout 1.0
    show isaac at left

    i "¿Ahhh?"

    e "Isaac se encuentra frente a una puerta gigantesca, algo que jamás había visto antes, y que le provoca un malestar profundo en el estómago."

    e "La puerta está grabada con patrones horribles y amorfos. Sus relieves parecen contar historias de desgracias y penas. Algunas escenas son demasiado espantosas como para describirse, y todas esas imágenes terribles convergen hacia el centro de la puerta…"

    e "Allí, tallado con precisión repugnante, está representado un monstruo tan espantoso que Isaac no podría haber imaginado ni en cien vidas."

    e "La insignificancia de su existencia ante semejante puerta lo paraliza. El dolor y el terror son tan intensos que, por un momento, preferiría estar en su casa siendo maltratado por su madre."

    scene bg_nivel_4_2

    e "Pero de pronto, un rugido profundo retumba. Es la puerta… moviéndose. Conforme se abre, una potente luz del otro lado empieza a inundar toda la habitación."


    if score == 3:

        e "El ambiente se vuelve más pesado, como si capas de aire denso atravesaran el cuerpo de Isaac obligándolo a avanzar solo un paso a la vez."

        e "Una desesperación visceral brota dentro de él, deseando terminar con todo en este mismo instante… porque cualquier cosa sería mejor que seguir soportando esa agonía."

        e "De repente, Isaac ya se encuentra dentro de la habitación… si es que puede llamarse habitación a un espacio donde no existen paredes ni techo visibles."

        e "Una pesadez abrumadora apenas le permite mantenerse de pie. Su cuerpo avanza por pura inercia, hasta que frente a él aparece una mesa de ajedrez… y un ser completamente distinto a cualquier monstruosidad que haya encontrado antes."
        
        show monstruo4 at right

        e "Su apariencia transmite una falsa sensación de calma y seguridad que contrarresta los malestares del lugar… pero Isaac sabe que no puede confiarse. Había leído que en el ajedrez la mente es todo, y bajar la guardia sería su fin."

    else:

        play music "music/F/Mischief Maker.mp3" fadeout 1.0

        scene oficina

        e "Al otro lado de la puerta se revela una enorme oficina. Monstruos de todas formas corren de un lado a otro con prisa frenética."

        e "Hay pilas de papeles por todos lados, documentos volando por el aire como si el caos fuera un empleado más."

        e "Al abrirse por completo la puerta, Isaac ve a un ser hecho completamente de luz, quien parece estar distraído hablando por… ¿un comunicador?"

        show monstruo4 at right

        m "Sí, por favor, recorre mi cita del jueves y compra unos regalos para los monstruos de las cuevas 6 y 7."

        e "El ser deja de hablar. Hace un gesto que indica que finalmente notó la presencia de Isaac, y se acerca de inmediato."

        m "Ay no puede ser… ya llegó. Eres tú, ¿verdad? Bueno, dudo que haya muchos niños corriendo por esta zona."

        m "Ya me contaron todo lo que has hecho y déjame decirte… no estoy muy contento."

        m "¿Ves TODO este caos? ¿Adivina de quién es la culpa?"

        i "¿Ehhh?"

        m "Exacto. Tuya. Lo ÚLTIMO que queríamos después de escapar era lidiar con alguien capaz de volver a sellarnos. Y menos con un niño tan molesto."

        e "El monstruo de luz gira violentamente hacia la derecha."

        m "¡¡¡BOOOOOOOB!!! ¡Trae el ajedrez! Voy a mandar a este niño a su casa."

        e "Regresa su mirada hacia Isaac."

        m "Muy bien. Te advierto que soy MUY bueno. Ni se te ocurra ganar o empatar, ¿entendido? Ya eres suficiente dolor de cabeza."


    $ chess_return_label = "cuarto_nivel"
    call chess_game from _call_chess_game_3

    if victoria:

        play music "music/H/Giant Wyrm.mp3" fadeout 1.0

        scene bg_nivel_4_3

        $ victoria = False

        e "Bajo sus pies, un agujero negro comienza a estremecerlo todo."

        e "Isaac entra en pánico al ver cómo el monstruo al que acaba de derrotar es succionado de inmediato, desintegrándose en el vacío."

        e "La mesa de ajedrez se rompe violentamente y también es absorbida."

        e "Isaac intenta nadar en el aire, moverse, escapar de la fuerza del agujero… cualquier cosa."

        e "En su visión periférica aparece lo que parece ser una pequeña hada hecha de luz, que le hace una señal para que la siga."

        e "Isaac flota hacia ella, alejándose del agujero oscuro. Por primera vez puede descansar un poco de tanta tensión, mientras avanza hacia un destino desconocido."


        
    elif empate:

        play music "music/F/Mischief Maker.mp3" fadeout 1.0

        $ empate = False

        e "Isaac le entrega el formulario al monstruo de luz."

        e "Este cae al suelo y el formulario termina golpeándole la cara."

        m "¿Por qué eres así? ¿Qué te hicimos para que nos hagas esto?"

        m "¿Es mucho pedir que nos dejes aniquilar a toda la humanidad y… de paso a ti? Eres tan egoísta, niño."

        m "Este papeleo será un dolor de cabeza… pero bueno, al menos me diste el formulario."

        m "Por favor, sigue a mi secretaria. Ella te guiará a la salida. Y POR FAVOR… JAMÁS regreses aquí."


    else:

        return

label epilogo:

    scene titulo_nivel_5
    "¿Final?"

    scene black

    e "Isaac avanzaba cerca de aquel ser que lo guiaba. No se sentía particularmente seguro, pero la enorme tensión de la partida pasada comenzaba a disiparse."

    e "Mientras caminaba, podía ver a la distancia un agujero que devoraba la poca luz restante tras aquel largo recorrido."

    e "A medida que se acercaba, Isaac sintió cómo su conciencia se debilitaba… y después…"

    e "Oscuridad."

    if score == 4:

        play music "music/At Lunch.mp3" fadeout 1.0 loop

        e "Isaac abre los ojos y se encuentra en el patio de su casa. El sol le pega en la cara, cálido y familiar, y siente un alivio inmenso."

        e "No sabe si lo que vivió fue un sueño, una pesadilla… o algo peor. Pero está feliz de haber escapado de aquella experiencia tan terrible."

        e "Mientras se levanta para entrar a su casa, nota algo detrás del árbol del patio."

        e "Allí, semiescondido, hay un agujero… cubierto con un tablero de ajedrez gastado. De entre las grietas escurre un líquido negro, viscoso, que de pronto se petrifica."

        e "Isaac retrocede un paso. Algo dentro de él le dice que no debería tocarlo. Jamás."

        scene ending_good

    elif score == 0:

        play music "music/F/March of the Spoons.mp3" fadeout 1.0 loop

        e "Isaac abre los ojos y frente a él… la secretaria."

        show monstruo4 at right

        m "Muy bien, niño. Ya contactamos a nuestro abogado."

        m "Aunque *en teoría* 'ganaste el juego' —sí, si ganaste, este es un ending—, realmente solo empataste contra TODOS nuestros empleados."

        m "Por lo tanto, tenemos dos caminos: uno, te demandamos y lo peleamos en la corte. Pero no podemos porque… ¿cuántos años tienes? ¿Cinco?"

        m "Así que decidimos regresarte en el tiempo para que comiences tu recorrido desde cero… y esta vez te vencemos, jejeje."

        m "¿Es tramposo? Sí. Definitivamente. Pero nuestro abogado lo aprobó. Ya sabes… ni siquiera es un monstruo, pero todos le tenemos miedo."

        m "Nos vemos pronto, niño."

        e "Y con esas palabras, la secretaria se disuelve en el viento."

        scene ending_bad
    
    else:

        play music "music/F/March of the Spoons.mp3" fadeout 1.0 loop

        e "Isaac abre los ojos y frente a él… está la secretaria."

        show monstruo5 at right

        m "Ok, niño. Pues nada mal. No fuiste el mejor oponente de esta empresa, pero tampoco el peor."

        m "Ganaste [score] partidas contra nuestros mejores elementos y empataste el resto, así que… bueno, tendremos que recuperarnos de esta humillación."

        m "Vendremos a visitarte cuando tengas diez años. —Si es que no pasa algo antes, jeje—"

        m "(Referencia a Isaac… este es el final canon de este juego, por si le interesa a los que lo están jugando, wink wink.)"

        m "En fin, solo puedo decirte que te prepares. Fue divertido, niño. Jamás había visto a mis superiores perder la cabeza por un niño que apenas habla, pero que por alguna razón sí sabe leer… y juega al ajedrez como un demonio."

        e "La secretaria desaparece en el aire con un parpadeo."

        e "Isaac sale corriendo hacia su casa a toda velocidad, escapando de la peor experiencia de su vida."

        e "Desde ese día decidió que odiaba la burocracia. Con toda su alma."

        scene ending_fanon

label creditos:
    
    scene black
    
    # Ocultar la ventana de diálogo para mostrar solo los créditos
    window hide
    
    # Pausa inicial
    pause 1.0
    
    # Título de los créditos
    centered "{size=60}{color=#ffffff}CRÉDITOS{/color}{/size}" with dissolve
    pause 2.0
    pause 0.5
    
    # Sección de roles principales
    
    centered "{size=40}{color=#ffffff}DIRECCIÓN{/color}{/size}\n{size=30}{color=#cccccc}Esekodrilo{/color}{/size}" with dissolve
    pause 2.5
    pause 0.5

    centered "{size=40}{color=#ffffff}MOTOR DE AJEDREZ{/color}{/size}\n{size=30}{color=#cccccc}Lynn Zheng{/color}{/size}" with dissolve
    pause 2.5
    pause 0.5

    centered "{size=40}{color=#ffffff}FOTOGRAFIA{/color}{/size}\n{size=30}{color=#cccccc}Michael Morse, Seven11nash{/color}{/size}" with dissolve
    pause 2.5
    pause 0.5
    
    centered "{size=40}{color=#ffffff}GUIÓN{/color}{/size}\n{size=30}{color=#cccccc}Esekodrilo{/color}{/size}" with dissolve
    pause 2.5
    pause 0.5
    
    centered "{size=40}{color=#ffffff}PROGRAMACIÓN{/color}{/size}\n{size=30}{color=#cccccc}Esekodrilo{/color}{/size}" with dissolve
    pause 2.5
    pause 0.5
    
    centered "{size=40}{color=#ffffff}ARTE 2D Y 3D{/color}{/size}\n{size=30}{color=#cccccc}Esekodrilo{/color}{/size}" with dissolve
    pause 2.5
    pause 0.5
    
    centered "{size=40}{color=#ffffff}MÚSICA{/color}{/size}\n{size=30}{color=#cccccc}Kevin MacLeod (incompetech.com) Licensed under Creative Commons: By Attribution 4.0 License{/color}{/size}" with dissolve
    pause 2.5
    pause 0.5
    
    centered "{size=40}{color=#ffffff}SONIDO{/color}{/size}\n{size=30}{color=#cccccc}Esekodrilo{/color}{/size}" with dissolve
    pause 2.5
    pause 1.0
    
    # Sección especial para jugadores beta
    centered "{size=50}{color=#ffff00}AGRADECIMIENTO ESPECIAL{/color}{/size}" with dissolve
    pause 2.0
    pause 0.5
    
    centered "{size=35}{color=#ffffff}Todo aquel que llegue a esta parte{/color}{/size}\n{size=30}{color=#cccccc}podrá estar aquí por haber acabado{/color}{/size}\n{size=30}{color=#cccccc}el juego en fase beta{/color}{/size}" with dissolve
    pause 4.0
    pause 1.0
    
    centered "{size=40}{color=#ffffff}¡Gracias por jugar!{/color}{/size}" with dissolve
    pause 3.0
    pause 1.0
    
    # Restaurar la ventana de diálogo
    window show
    
    return

#endregion

# Pantalla de botones de prueba (solo visible en modo desarrollador)
screen chess_test_buttons(test_player_color):
    zorder 1000
    if config.developer:
        frame:
            xalign 0.02
            yalign 0.02
            background "#000000cc"
            padding (10, 10)
            vbox spacing 5:
                text "TEST BUTTONS" color "#fff" size 16
                textbutton "Simular Victoria":
                    action [
                        SetVariable("_return", test_player_color),
                        Return(test_player_color)
                    ]
                    text_color "#0f0"
                textbutton "Simular Empate":
                    action [
                        SetVariable("_return", DRAW),
                        Return(DRAW)
                    ]
                    text_color "#ff0"

#region chess handle
# Inicialización del motor de ajedrez (solo se ejecuta UNA VEZ al inicio del juego)
label init_chess_engine:
    # Inicializa el motor Stockfish solo si no existe
    if 'STOCKFISH_ENGINE' not in global_objects or global_objects['STOCKFISH_ENGINE'] is None:
        $ global_objects['STOCKFISH_ENGINE'] = chess.engine.SimpleEngine.popen_uci(STOCKFISH, startupinfo=STARTUPINFO)
    return

# Label para jugar ajedrez (se puede llamar múltiples veces)
# Antes de llamar este label, establece chess_return_label con el label al que volver si pierdes
# Ejemplo: $ chess_return_label = "primer_nivel"
label chess_game:
    # Configuración de la partida (necesario cada vez)
    $ fen = STARTING_FEN
    $ player_color = chess.WHITE # this constant is defined in chess_displayable.rpy
    
    # Asegurar que el motor esté inicializado
    call init_chess_engine from _call_init_chess_engine
    
    window hide
    $ quick_menu = False

    # avoid rolling back and losing chess game state
    $ renpy.block_rollback()

    # disable Esc key menu to prevent the player from saving the game
    $ _game_menu_screen = None

    # Mostrar botones de prueba si está en modo desarrollador
    if config.developer:
        show screen chess_test_buttons(player_color)

    call screen chess(fen, player_color, depth)
    
    # Ocultar botones de prueba después del juego
    if config.developer:
        hide screen chess_test_buttons

    # re-enable the Esc key menu
    $ _game_menu_screen = 'save'

    # avoid rolling back and entering the chess game again
    $ renpy.block_rollback()

    # restore rollback from this point on
    $ renpy.checkpoint()

    $ quick_menu = True
    window show

    if _return == DRAW:
        e "EMPATE"
        $ empate = True
        return

    else: # RESIGN or CHECKMATE
        $ winner = "Isaac" if _return == chess.WHITE else "EL MAL"
        if player_color is not None: # PvC
            if _return == player_color:
                e "GANADOR: [winner]."
                $ score +=1
                $ depth +=1
                $ victoria = True
                return
            else:
                scene game_over
                e "Todo está perdido...."
                jump lose


label lose:
    menu:
        "..."

        "No,volvamos a jugar":
            # Volver al label especificado antes de la partida, o cerrar el motor si no hay label
            if chess_return_label:
                $ return_label = chess_return_label
                $ chess_return_label = None  # Limpiar el identificador
                jump expression return_label
            else:
                jump cleanup_chess_engine

        "Lo siento, Isaac":
            jump cleanup_chess_engine

# Label para cerrar el motor de ajedrez (llamar al final del juego completo)
# Úsalo cuando el juego termine completamente para liberar recursos
label cleanup_chess_engine:
    $ quit_stockfish()
    return

#endregion
from django.shortcuts import render
from django.http import Http404

# ─────────────────────────────────────────────────────────────
# Datos de prueba — serán reemplazados por modelos de base de datos
# ─────────────────────────────────────────────────────────────
posts = [
    {
        'autor': 'Destiny Franks',
        'titulo': 'El futuro de la IA en los videojuegos',
        'contenido': (
            'La inteligencia artificial está transformando la industria del gaming. '
            'Desde NPCs con comportamientos más realistas hasta generación procedural de mundos, '
            'el futuro promete experiencias inimaginables.'
        ),
        'fecha': '7 de agosto, 2024',
    },
    {
        'autor': 'Juan Pérez',
        'titulo': 'Django vs FastAPI: ¿cuál elegir en 2024?',
        'contenido': (
            'Comparamos dos de los frameworks Python más populares para desarrollo web. '
            'Analizamos rendimiento, escalabilidad y ecosistema para ayudarte a tomar la mejor decisión.'
        ),
        'fecha': '15 de septiembre, 2024',
    },
    {
        'autor': 'Ana Gómez',
        'titulo': 'Configurando tu setup gamer ideal',
        'contenido': (
            'Periféricos, iluminación y ergonomía: todo lo que necesitas saber para armar '
            'tu estación de trabajo perfecta sin arruinarte en el intento.'
        ),
        'fecha': '3 de octubre, 2024',
    },
]

# ────────────────────────────────────────────────────────────────────
# Posts de ejemplo — serán reemplazados por modelos de base de datos
# ────────────────────────────────────────────────────────────────────
lista_posts = [
    {
        'id': 1,
        'slug': 'valorant-agente-waylay-episodio-9',
        'titulo': 'Valorant revela a Waylay: el agente que rompe el meta en el Episodio 9',
        'extracto': 'Riot Games confirmó al nuevo agente: Waylay, una duelista australiana con habilidades cinéticas que promete redefinir los duelos y la dinámica de post-plants en Valorant.',
        'contenido': """
<p>Riot Games ha roto el silencio y revelado oficialmente a <strong>Waylay</strong>, la nueva duelista que llegará en el Episodio 9, Acto 2. De origen australiano y con pasado en operaciones de alto riesgo, fue expuesta a radiante durante una misión fallida que le otorgó el control sobre las fuerzas cinéticas.</p>
<h3>Sus habilidades</h3>
<ul>
<li><strong>Acelerón (Q):</strong> Se lanza hacia adelante dejando un rastro de energía que aumenta la velocidad de aliados durante 4 segundos.</li>
<li><strong>Ruptura (E):</strong> Emite una onda de choque radial que desplaza enemigos y destruye utilidad en el área.</li>
<li><strong>Trayectoria (C):</strong> Lanza un proyectil que rebota una vez antes de detonar. Ideal para despejar esquinas.</li>
<li><strong>Colapso — Ultimate (X):</strong> Crea una zona de gravedad inversa en 15 metros de radio. Los enemigos dentro quedan suspendidos 3 segundos.</li>
</ul>
<h3>Impacto en el meta competitivo</h3>
<p>Los analistas del VCT ya señalan que el ultimate de Waylay podría ser devastador en situaciones de post-plant y en defensas de sitio. Varios equipos de la escena profesional han comenzado a revisar sus composiciones para integrar al nuevo agente desde el primer día de lanzamiento.</p>
<p>La comunidad ha reaccionado con entusiasmo, aunque ya hay voces que alertan sobre un posible overtuning del ultimate. Riot aseguró que el balance será monitoreado de cerca durante las primeras semanas del parche.</p>
""",
        'categoria': 'Valorant',
        'fecha': '2025-05-28',
        'fecha_display': '28 de mayo, 2025',
        'autor': 'Carlos Mendoza',
        'tiempo_lectura': '5 min',
        'icono': 'fas fa-crosshairs',
    },
    {
        'id': 2,
        'slug': 'fortnite-capitulo-6-temporada-7-glaciares',
        'titulo': 'Fortnite Cap. 6 T7: glaciares, temperatura corporal y la colaboración con Dune',
        'extracto': 'La nueva temporada congela la isla con un bioma ártico masivo, introduce el sistema de temperatura corporal como mecánica de supervivencia y confirma la llegada del universo de Dune.',
        'contenido': """
<p>Epic Games arrancó la <strong>Temporada 7 del Capítulo 6</strong> con uno de los mapas más espectaculares de la historia del juego. Un glaciar masivo ha sepultado el norte de la isla, creando un contraste dramático con los biomas exuberantes que florecen en el sur.</p>
<h3>Nuevas localizaciones</h3>
<ul>
<li><strong>Puerto Helado:</strong> Puerto industrial congelado, ideal para botín de larga distancia.</li>
<li><strong>La Grieta:</strong> Cañón de hielo repleto de cuevas y rutas alternativas.</li>
<li><strong>Cúpula Cero:</strong> Laboratorio subterráneo con el mejor loot de la temporada.</li>
</ul>
<h3>Sistema de temperatura corporal</h3>
<p>La gran novedad es el <strong>medidor de temperatura</strong>: permanecer en zonas árticas sin equipamiento adecuado reducirá tu salud progresivamente. Para contrarrestarlo, deberás recoger ropa de abrigo, encender hogueras o consumir alimentos calientes distribuidos por el mapa.</p>
<h3>Colaboración con Dune</h3>
<p>Epic confirmó la colaboración con el universo de <em>Dune</em>. Los skins de Paul Atreides, Lady Jessica y el Guardián Fremen ya están disponibles en la tienda. Como novedad, el Sandworm aparece como evento LTM durante los primeros 15 días de temporada, destruyendo estructuras y otorgando loot premium a quien logre escapar de su trayectoria.</p>
""",
        'categoria': 'Fortnite',
        'fecha': '2025-06-01',
        'fecha_display': '1 de junio, 2025',
        'autor': 'Sofía Ramírez',
        'tiempo_lectura': '6 min',
        'icono': 'fas fa-gamepad',
    },
    {
        'id': 3,
        'slug': 'vct-champions-2025-sentinels-campeon',
        'titulo': 'VCT Champions 2025: Sentinels se corona campeón del mundo en épica final',
        'extracto': 'En una final histórica de cinco mapas, Sentinels derrotó a NaVi con una actuación monumental de TenZ para alzar el trofeo del VCT Champions 2025 ante más de 3,4 millones de espectadores en línea.',
        'contenido': """
<p>El <strong>VCT Champions 2025</strong> quedará grabado como uno de los momentos más épicos de la historia de los esports. La final en el Crypto.com Arena de Los Ángeles enfrentó a <strong>Sentinels</strong> y <strong>Natus Vincere</strong> en una batalla de cinco mapas que mantuvo al público en vilo durante más de seis horas.</p>
<h3>Resumen de la final</h3>
<p>Sentinels dominó el primer mapa, Ascent, gracias a una configuración defensiva impecable. NaVi respondió en Pearl para igualar la serie. Los mapas 3 y 4 fueron un intercambio de golpes con actuaciones brillantes de ambos equipos, llevando la final al esperado mapa decisivo: Lotus.</p>
<p>En el mapa final, TenZ salió encendido con un impresionante 32/18/10, liderando la remontada histórica de Sentinels para cerrar la serie 3-2.</p>
<h3>TenZ, MVP del torneo</h3>
<p>Tyson "TenZ" Ngo fue elegido MVP con un ACS promedio de 298 a lo largo de todo el torneo. En rueda de prensa, el jugador canadiense emocionó al público al dedicar el trofeo a su familia y a los fans que lo apoyaron durante los años más difíciles de su carrera.</p>
<h3>Cifras del evento</h3>
<p>El VCT Champions 2025 repartió un prize pool de <strong>2,25 millones de dólares</strong>, el más alto en la historia del juego. El pico de <strong>3,4 millones de espectadores simultáneos</strong> también marcó un récord histórico para el circuito oficial de Riot Games.</p>
""",
        'categoria': 'eSports',
        'fecha': '2025-05-15',
        'fecha_display': '15 de mayo, 2025',
        'autor': 'Andrés Torres',
        'tiempo_lectura': '7 min',
        'icono': 'fas fa-trophy',
    },
    {
        'id': 4,
        'slug': 'gpt5-openai-records-razonamiento-cientifico',
        'titulo': 'GPT-5 de OpenAI: nuevos récords en matemáticas, código y razonamiento científico',
        'extracto': 'OpenAI presentó su modelo más avanzado con resultados que superan todos los benchmarks conocidos en matemáticas, física y programación, gracias a un nuevo modo de razonamiento profundo de varios minutos.',
        'contenido': """
<p>OpenAI ha lanzado oficialmente <strong>GPT-5</strong>, el modelo de lenguaje más potente de la compañía hasta la fecha. Los resultados en benchmarks de razonamiento técnico lo posicionan como el sistema más capaz disponible públicamente en múltiples disciplinas científicas.</p>
<h3>Resultados en benchmarks clave</h3>
<ul>
<li><strong>MATH-500:</strong> 98,1% de precisión (récord absoluto en matemáticas avanzadas)</li>
<li><strong>HumanEval — código Python:</strong> 96,2%</li>
<li><strong>GPQA Diamond — preguntas de doctorado:</strong> 91,5%</li>
<li><strong>SWE-bench Verified — problemas reales de GitHub:</strong> 75,3% resueltos</li>
</ul>
<h3>Razonamiento profundo</h3>
<p>GPT-5 introduce un modo de razonamiento que le permite reflexionar internamente durante varios minutos antes de entregar su respuesta, identificando y corrigiendo errores en su propio proceso de pensamiento. Esta arquitectura es especialmente efectiva en problemas de múltiples pasos y en proyectos de ingeniería complejos.</p>
<h3>Impacto en la industria tech y gaming</h3>
<p>Empresas de los sectores farmacéutico, financiero y de ingeniería ya reportan mejoras significativas en productividad. Varios estudios de videojuegos también exploran su uso para generación procedural de narrativas, diseño de sistemas de juego y creación de comportamientos avanzados en NPCs.</p>
""",
        'categoria': 'Inteligencia Artificial',
        'fecha': '2025-06-05',
        'fecha_display': '5 de junio, 2025',
        'autor': 'María Fernández',
        'tiempo_lectura': '8 min',
        'icono': 'fas fa-robot',
    },
    {
        'id': 5,
        'slug': 'cs2-major-paris-navi-campeon-s1mple-retiro',
        'titulo': 'CS2 Major París: NaVi arrasa y s1mple anuncia su retiro tras la victoria',
        'extracto': 'Natus Vincere ganó el Major de París con una actuación histórica de s1mple, quien justo tras levantar el trofeo anunció su retiro del CS2 profesional entre lágrimas y ovación del público.',
        'contenido': """
<p>El <strong>CS2 Major de París 2025</strong> quedará grabado como uno de los momentos más emotivos de la historia del Counter-Strike. Natus Vincere se coronó campeón tras vencer a FaZe Clan en la gran final, pero el resultado deportivo quedó eclipsado por el anuncio que todos temían.</p>
<h3>La final</h3>
<p>NaVi dominó la final en tres mapas: Mirage, Anubis y Ancient. s1mple cerró el torneo con un rating de <strong>1.42</strong>, el más alto registrado en cualquier Major de la historia del Counter-Strike, según los registros de HLTV.</p>
<h3>El anuncio del retiro</h3>
<p>Minutos después de levantar el trofeo, Oleksandr "s1mple" Kostyliev tomó el micrófono y, con la voz quebrada, anunció su retirada del CS2 competitivo. <em>"He dado todo lo que tenía a este juego. Es momento de descansar y vivir mi vida fuera de las competiciones"</em>, declaró ante el silencio y los aplausos del Accor Arena.</p>
<h3>El legado de s1mple</h3>
<p>Con <strong>7 títulos de Major</strong>, 6 premios HLTV al Mejor Jugador del Año y casi una década en el circuito profesional, s1mple es ampliamente considerado el mejor jugador de Counter-Strike de todos los tiempos. Su retiro marca el fin de una era en los esports mundiales.</p>
""",
        'categoria': 'eSports',
        'fecha': '2025-04-20',
        'fecha_display': '20 de abril, 2025',
        'autor': 'Andrés Torres',
        'tiempo_lectura': '6 min',
        'icono': 'fas fa-trophy',
    },
    {
        'id': 6,
        'slug': 'fortnite-colaboracion-attack-on-titan-2025',
        'titulo': 'Fortnite x Attack on Titan: skins, emotes y el modo LTM "Operación Muralla"',
        'extracto': 'Epic Games confirma la colaboración más esperada del año: Eren, Mikasa y Levi regresan a la isla con skins rediseñadas y un modo LTM donde los jugadores se convierten en Titanes Colosales.',
        'contenido': """
<p>Epic Games y Kodansha han confirmado la segunda colaboración entre <strong>Fortnite y Attack on Titan</strong>. Llega el 20 de junio y estará activa durante tres semanas con el mayor paquete de contenido cruzado del año.</p>
<h3>Skins disponibles</h3>
<ul>
<li><strong>Eren Jaeger</strong> — con el Titán Fundador disponible como estilo alternativo</li>
<li><strong>Mikasa Ackerman</strong> — emote exclusivo con animación de maniobras en 3D</li>
<li><strong>Levi Ackerman</strong> — skin más esperada, con efecto reactivo de daño al eliminar</li>
<li><strong>Historia Reiss</strong> — exclusiva del battle pass de la temporada actual</li>
</ul>
<h3>LTM: Operación Muralla</h3>
<p>El modo de juego temporal enfrenta a dos equipos: 10 jugadores como Exploradores con picos de maniobras en 3D funcionales, contra 5 jugadores en rol de Titanes Colosales con estadísticas amplificadas. Los Exploradores deben completar objetivos en el mapa antes de ser eliminados.</p>
<h3>Objetos adicionales</h3>
<p>El paquete incluye el Pico de Maniobras en 3D como hacha de recolección, un planeador con las Alas de la Libertad y varios mochileros temáticos. Todo disponible por separado en la tienda o en dos bundles por tiempo limitado.</p>
""",
        'categoria': 'Fortnite',
        'fecha': '2025-06-08',
        'fecha_display': '8 de junio, 2025',
        'autor': 'Sofía Ramírez',
        'tiempo_lectura': '4 min',
        'icono': 'fas fa-gamepad',
    },
    {
        'id': 7,
        'slug': 'valorant-parche-10-nerf-clove-buffs-yoru',
        'titulo': 'Parche 10.0 de Valorant: nerf masivo a Clove y buffs a agentes olvidados del meta',
        'extracto': 'El parche más grande del año llega a Valorant: Clove recibe su nerf más severo en meses mientras Yoru, Neon y Fade obtienen mejoras sustanciales para volver a ser viables en el meta competitivo.',
        'contenido': """
<p>Riot Games publicó las notas del <strong>Parche 10.0 de Valorant</strong>, el más extenso desde el lanzamiento del juego, con cambios que impactarán directamente en el meta clasificatorio y competitivo.</p>
<h3>Nerf a Clove</h3>
<p>Clove, la agente más elegida del meta en los últimos tres actos, sufre cambios significativos en su ultimate <em>No Mueres Aquí</em>: el tiempo de invulnerabilidad se reduce de 4 a 2,5 segundos, el radio de reaparición disminuye un 20% y su habilidad de humo pasa de 3 a 2 cargas.</p>
<h3>Buffs a Yoru</h3>
<p>El buff más esperado de la comunidad: los señuelos de Yoru ahora disparan en ráfagas automáticas similares a las del jugador real, haciéndolos prácticamente indistinguibles durante el fragor del combate.</p>
<h3>Buffs a Neon y Fade</h3>
<p>Neon reduce el tiempo de recarga de su sprint y su ultimate puede alcanzar 3 objetivos antes de agotarse (antes eran 2). Fade ve mejorada la duración de su Delirio de 12 a 15 segundos, haciéndola más viable para composiciones de control.</p>
<h3>Cambios geométricos en Sunset</h3>
<p>El parche también elimina el famoso pixel walk en A Main y amplía ligeramente el corredor de B Site para facilitar las entradas y reducir las ventajas excesivas de los defensores.</p>
""",
        'categoria': 'Valorant',
        'fecha': '2025-05-10',
        'fecha_display': '10 de mayo, 2025',
        'autor': 'Carlos Mendoza',
        'tiempo_lectura': '5 min',
        'icono': 'fas fa-crosshairs',
    },
    {
        'id': 8,
        'slug': 'ia-generativa-npcs-videojuegos-dialogos-infinitos',
        'titulo': 'La IA generativa transforma los NPCs: adiós a los diálogos predefinidos para siempre',
        'extracto': 'Los grandes estudios están adoptando modelos de lenguaje para crear NPCs con conversaciones infinitas, memoria persistente y personalidades únicas que evolucionan según el comportamiento del jugador.',
        'contenido': """
<p>La integración de la <strong>inteligencia artificial generativa</strong> en el desarrollo de videojuegos alcanza un punto de inflexión. Estudios como Ubisoft, EA y decenas de equipos indie ya implementan modelos de lenguaje para redefinir la forma en que los NPCs interactúan con los jugadores.</p>
<h3>Ubisoft NEO NPC</h3>
<p>El proyecto <em>NEO NPC</em> de Ubisoft, presentado en la GDC 2025, mostró personajes capaces de mantener conversaciones sin guion basándose en el estado del mundo del juego, la historia del jugador y el contexto de la partida. Los NPCs recuerdan interacciones previas y ajustan su actitud según el comportamiento acumulado del usuario.</p>
<h3>Inworld AI: el middleware del futuro</h3>
<p>La startup <strong>Inworld AI</strong> se posiciona como el proveedor de infraestructura de IA conversacional para videojuegos, con contratos confirmados con tres de los diez estudios más grandes del mundo. Su plataforma permite crear "cerebros" de NPC con personalidad, emociones, objetivos propios y memoria a largo plazo.</p>
<h3>Desafíos y riesgos</h3>
<p>Los desarrolladores advierten sobre los retos de mantener coherencia narrativa cuando los NPCs generan respuestas impredecibles. El filtrado de contenido inapropiado y la consistencia con el tono artístico del juego son los principales obstáculos técnicos. A pesar de ello, el consenso en la industria es claro: los NPCs con diálogos predefinidos tienen los días contados.</p>
""",
        'categoria': 'Inteligencia Artificial',
        'fecha': '2025-06-03',
        'fecha_display': '3 de junio, 2025',
        'autor': 'María Fernández',
        'tiempo_lectura': '9 min',
        'icono': 'fas fa-robot',
    },
]


def inicio(request):
    """Vista principal con búsqueda, filtro por categoría y ordenamiento."""
    query     = request.GET.get('q', '').strip()
    categoria = request.GET.get('categoria', '').strip()
    orden     = request.GET.get('orden', 'reciente').strip()

    resultado = lista_posts[:]

    # Filtrar por término de búsqueda
    if query:
        q = query.lower()
        resultado = [
            p for p in resultado
            if q in p['titulo'].lower()
            or q in p['extracto'].lower()
            or q in p['contenido'].lower()
            or q in p['categoria'].lower()
            or q in p['autor'].lower()
        ]

    # Filtrar por categoría
    if categoria:
        resultado = [
            p for p in resultado
            if p['categoria'].lower() == categoria.lower()
        ]

    # Ordenar por fecha
    resultado.sort(key=lambda p: p['fecha'], reverse=(orden != 'antiguo'))

    # Categorías únicas para los botones de filtro
    categorias = sorted({p['categoria'] for p in lista_posts})

    contexto = {
        'posts':            resultado,
        'categorias':       categorias,
        'query':            query,
        'categoria_activa': categoria,
        'orden_activo':     orden,
        'total_resultados': len(resultado),
        'total_posts':      len(lista_posts),
        'title':            'Inicio',
    }
    return render(request, 'blog/home.html', contexto)


def detalle_post(request, slug):
    """Vista de detalle de un post individual buscado por slug."""
    post = next((p for p in lista_posts if p['slug'] == slug), None)
    if post is None:
        raise Http404('Post no encontrado.')

    # Posts relacionados: misma categoría, máximo 3
    relacionados = [
        p for p in lista_posts
        if p['categoria'] == post['categoria'] and p['slug'] != slug
    ][:3]

    contexto = {
        'post':        post,
        'relacionados': relacionados,
        'title':       post['titulo'],
    }
    return render(request, 'blog/detalle_post.html', contexto)


def acerca(request):
    """Vista de la página 'Acerca de'."""
    return render(request, 'blog/acerca.html', {'title': 'Acerca de'})


def contacto(request):
    """Vista de la página de contacto."""
    return render(request, 'blog/contacto.html', {'title': 'Contacto'})


def registro(request):
    """Vista del formulario de registro de usuario."""
    return render(request, 'blog/registro.html', {'title': 'Crear cuenta'})


def login_vista(request):
    """Vista del formulario de inicio de sesión."""
    return render(request, 'blog/login.html', {'title': 'Iniciar Sesión'})
# Déclaration des personnages
define swan = Character('???', color="#c8ffc8")
define petite = Character('???', color="#c8ffc8")
define grande = Character('???', color="#c8ffc8")
define yeonho = Character('???', color="#c8ffc8")

# CG
# TODO images des perso à redimensionner

image CG_miroir_swan = "CG_miroir_swan.jpg"

# Début du jeu
label start:
    "Il y a de cela plusieurs dizaines d'années,\nune légende fit son apparition."
    "Celle de cris venant du manoir de la défunte sorcière."
    "Certains disent qu'il s'agit de ses cris d'agonie."
    "D'autres disent qu'il s'agit d'expériences qu'elle aurait fait en secret"
    "Mais personne ne connait la vérité..."

    # Arc 1 : Le manoir
        #inserer bg

    swan "Ouch..."

    "Je me réveille, le dos en compote, après ce qui semble être plusieurs heures de sommeil à même le sol."
    "En observant les alentours, je me rends vite compte que le lieu semble abandonné et peu acceillant."

    swan "Ça donne la chair de poule… "
    swan "Comment j'ai fait pour m'endormir ici moi…"
    swan "Attends…"
    swan "Comment je suis arrivée ici ? Avec qui ?"

    "J'ai essayé de fouiller dans mes souvenirs."

    "Mot-clé : \"essayé\" "

    "Je ne me rappelle de rien. De rien sauf ..."

    swan "Swan ... Je suppose ... Que c'est comme ça qu'on m'appelle ... ?"

    "Avec si peu d'informations et le lieu que je ne connaissais pas, j'étais complétement perdue."
    "Comment j'ai bien pu faire pour me retrouver dans cette situation ?!"

    $swan = Character('Swan', color="#c8ffc8")

    swan "... ARGHHHH !"
    swan "Pas le temps de se morfondre ! Ça va pas m'aider !"
    "Fouillons les alentours, je trouverais sûrement quelque chose d'intéressant."

    default g = False
    default d = False

label salle:

    if g != d and ( g or d ) :
        "En ressortant de la première salle, j'observais où aller."
    scene

    if g == d and g:
        jump secret

    if g:
        show mc neutral

menu:
    "Porte à gauche" :
        if g == d and d == False:
            "Je me dirige vers la porte à gauche dans mon champs de vision."
            "En me rapporchant, je me rends compte que la porte est remplie de dessins complexes, tout comme la poignée"
            "En poussant la porte, je rentre dans la pièce éclairée faiblement par la lumière de la lune traversant la fenêtre"
            "La pleine lune"
            "Mes yeux s'adaptent et me laissent découvrir la salle, inspectant chaque recoin"

        jump jeu

    "Porte à droite" :
        if g == d and d == False:
            "Je me dirige vers la porte à gauche dans mon champs de vision."
            "En me rapporchant, je me rends compte que la porte est remplie de dessins complexes, tout comme la poignée"
            "En poussant la porte, je rentre dans la pièce éclairée faiblement par la lumière de la lune traversant la fenêtre"
            "La pleine lune"
            "Mes yeux s'adaptent et me laissent découvrir la salle, inspectant chaque recoin"

        jump soeur

label jeu:
    $g = True
    scene salle_de_jeu
    swan "Une salle de jeu... Et très peu rangée... On croirait presque qu'une tempête est passée avant moi... "
    "Des poupées jonchaient le sol, recouvrant une partie de la pièce."
    "En tournant la tête vers la droite, je m'étonnais à croiser mon reflet."

    swan "Un miroir..."

    scene CG_miroir_swan

    "Je m'étonnais à fixer mon reflet."
    "Mes cheveux blonds en deux couettes cadrait mon visage pâle, ainsi que mes yeux vert jade."
    "Mon haut noir recouvrait un pull crème, le tout coincé dans un short marron clair, avec une veste bleue, un peu petite pour moi, faisant office de ceinture."
    "Sur mon poignet, au-dessus du pull, se logeait un bracelet rouge."
    "Mes chaussettes remontaient le long de mes jambes pour s'arrêter au milieu de mes cuisses, et une paire de bottines noires se trouvaient sur mes pieds."
    "Mais ce qui me choquait était le papillon jaune sur ma joue droite."
    "Et comme pour me prouver que ce n'était pas normal, je vis ce dernier battre des ailes pendant un instant."
    "Je secouais la tête pour me défaire de mon reflet et tournais la tête à gauche."

    scene salle_de_jeu

    "De ce côté, se trouvait une étagère, avec une multitude de peluches posées tout le long."
    "Certaines avaient un oeil en moins ou un bras qui ne tenait presque plus..."
    "Toute cette scène me donnait des frissons dans le dos."
    "Ayant fini de chercher, je rouvris la porte et sortis."

    jump salle

label soeur:
    $d = True
    scene
    if g:
        show mc neutral

    "On pouvait y discerner un lit et une armoire, ainsi qu'un bureau et une petite étagère."

    if g:
        show mc doubt
    swan "La chambre d'une petite fille je suppose, d'après le décor ... "
    "Les couvertures du lit étaient d'un rose pâle et jaune pastel, avec plusieurs peluches à côté des oreillers."
    "En regardant dans l'armoire, mes suppositions devinrent des affirmations suite au nombre de robes et d'accessoires présents."

    if g:
        show mc neutral
    "Pour trouver des informations, je me suis dirigée vers le bureau, espérant trouver quelque chose d'intéressant."
    swan "Une photo ... sûrement la propriétaire de la chambre ... "
    "Une petite fille blonde aux yeux émeraudes souriait à la caméra, une peluche à la main, dans ce qui ressemblait à un jardin."
    "Ne voulant pas fouiller dans des choses trop personnelles, j'ai décidé de sortir de la pièce."

    jump salle

label secret:
    show mc stressed
    swan "Bon, c'est bien beau tout ça, mais j'ai toujours aucune information ..."
    "Et en me triturant le cerveau, je remarquais la porte derrière l'endroit où je m'étais réveillée..."
    swan "Et dire que je l'avais même pas remarquée ..."
    "Ne voulant pas trop m'enfoncer dans un lieu inconnu, j'ouvris cette dernière porte, espérant trouver plus que dans les deux autres salles sur le pourquoi du comment je suis arrivée ici."

    scene
    show mc neutral
    swan "Une autre chambre... Pour quelqu'un de plus âgé vu la taille du lit ..."
    "Cette chambre avait les mêmes meubles que la précédente, un lit, une armoire, un bureau et une étagère."
    "Elle était cependant moins féminine. La seule manière de savoir était les vêtements dans l'armoire, qui comportaient des robes, des chemises, des jeans et des t-shirts."
    swan "Cherchons au même endroit que la précédente chambre, je trouverais peut être quelque chose cette fois..."
    "Après avoir fermé l'armoire, je me tournais vers le bureau, et comme dans la chambre précédente, la photo de la propriétaire de la chambre était présente."

    show mc shocked
    swan "Qu'est-ce que ... quoi ?"
    "Une fille aux cheveux blonds me ressemblant comme deux gouttes d'eau se tenait sur la photo."
    "Elle souriait et tenait un bouquet de fleurs fait à la va-vite, avec une couronne de fleurs sur la tête, s'accordant à la robe d'été qu'elle portait."
    "La seule différence étant le papillon non présent sur le visage de la jeune fille."

    petite "Tiens, qu'est-ce qu'elle fait là ?"
    hide mc neutral
    show mc shocked at left
    swan "Ahhh !!!"

    #show les deux filles

    "Mon cou me faisait mal après m'être retournée si brusquement, ne m'attendant pas à entendre une voix dans la pièce normalement vide."
    "Deux personnes en face de la bibliothèque me regardaient et, comme si cela était la chose la plus normale, une des deux, la plus petite, s'approcha de moi."

    petite "Tu crois qu'elle est arrivée en même temps que l'autre ?"
    grande "Il y a beaucoup de chance, oui. Mais elle n'était sûrement pas prévue."
    petite "Tu penses qu'elle aura des problèmes à cause de ça ?"
    grande "Évidement, c'est une personne extérieure."

    "Les deux personnes, que j'ai identifiées comme étant des filles, se parlaient, en oubliant presque que j'étais présente."
    "Pendant leur discussion, j'ai décidé de les observer, et en regardant de plus près, j'ai pu apercevoir quelque chose qui ne devrait pas se trouver là."

    swan "Des oreilles de panda ... "
    "Les deux filles" "Hmm ?"

    "Mince, j'ai leur attention !!!"

    petite "Dis, est-ce que tu sais ce que tu fais ici ?"
    show mc neutral at left
    swan "Non ..."
    petite "Comme ce qu'on pensait..."
    grande "Je te conseille de chercher ces livres dans le bâtiments, ils pourraient t'être très utiles."

    "Celle qui était toujours près de la bibliothèque pointa vers un livre."
    show mc asking at left
    "En m'approchant, je vis que le livre en question ressemblait à une histoire pour enfants. La couverture n'avait qu'un mot, « Swan »."

    swan "Mais qu'est-ce qui se passe ici à la fin… Vous êtes-"
    #hide les deux filles
    "J'allais demander aux deux filles panda ce qu'elles savaient, mais en me retournant, elles avaient disparu."

    show mc shocked
    swan "Quoi ?! Mais elles étaient la il y a deux secondes !!"
    "N'ayant rien de mieux à faire qu'écouter leur conseil, j'ouvris le conte."

    scene
    # debut du conte

    "Premier chapitre :"
    "Il y a bien longtemps vivait une jeune sorcière."
    "Cheveux blonds sales, vêtements en lambeaux, elle déambulait dans la forêt à la recherche de la nourriture qu'elle mangerait au prochain repas."
    "Ses yeux verts scrutaient les alentours pour trouver des baies ou un animal facile à attraper."
    "Mais au lieu de tomber sur un buisson de fraises des bois, ou bien un lapin inoffensif, ses yeux se posèrent sur une dame, assise sur le reste d'un tronc d'arbre coupé."
    "En s'attardant sur sa figure, elle n'avait pas remarqué que cette dernière l'observait également, pleine de curiosité et d'excitation suite à cette rencontre inattendue."
    "L'enfant n’eut pas le temps de réagir que la dame la prit dans ses bras, la serrant très fort comme si elle allait s'envoler la seconde d'après."
    "En la relâchant, l'enfant remarqua le panier d'herbes à côté de la souche, et s'en approcha."
    "Elle sorti une plante à l'apparence commune, et la jeta par terre en disant «Non.»."
    "La dame, étonnée de cette intervention, lui demanda alors pourquoi, ce pour quoi elle eut comme réponse «Toxique.»."

    # fin du conte

    scene
    show mc neutral

    swan "...Cette histoire me rappelle vaguement quelque chose..."
    yeonho "Tiens, qu'est-ce que tu fais là, petite ?"

    hide mc neutral
    show mc shocked at left
    swan "AHHH !"
    #show at right
    yeonho "Oh ? Je t'ai fais peur ? J'en suis navrée, ce n'était pas mon but."

    hide mc shocked
    show mc stressed at left
    "Encore une ... d'où est-ce qu'elles sortent à la fin ?!"
    swan "Est-ce qu'on pourrait enfin m'expliquer ce qu'il se passe... ?"

    yeonho "Bien sûr ! Avant de commencer, je m'appelle Yeonho, et je vis dans ce manoir !"
    $yeonho = Character('Yeonho', color="#c8ffc8")

    #hide mc stressed
    show mc doubt at left
    swan "Enchantée, je suppose..."
    yeonho "Cet endroit est une réalité alternative, ou monde parallèle, si tu préfère."
    yeonho "Tu as été amenée ici contre ton gré et ton cerveau a lancé un système de défense pour réagir, ce qui explique ta perte de mémoire."

    #hide mc doubt
    show mc asking at left
    swan "Je vois... Mais comment t'es au courant que je ne me rappelle de rien ?!"
    yeonho "Fufufu, j'ai des oreilles partout petite, et tes paroles peuvent confirmer mes propos."

    "Je baissais la tête, embarrassée."

    #hide mc asking
    show mc neutral at left
    swan "Il va vraiment falloir que je fasse attention à ce que je dis..."
    swan "Sinon, tu connais un moyen de sortir d'ici ? Et de récupérer ma mémoire ?"
    swan "Pas que j'aime pas l'endroit, mais c'est légèrement effrayant et je préfère rentrer chez moi intacte..."

    "Mais en relevant la tête..."

    #hide mc neutral
    scene
    show mc angry
    swan "Elle aussi elle a disparu sans rien dire ?! Pourquoi personne ne m'aide ici ?!"

    "Je suis donc sortie de la chambre qui semblait m'appartenir et partie chercher la sortie de cet endroit."

    #Arc 2
    scene

    "A suivre ..."
    return

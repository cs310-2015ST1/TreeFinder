from django import forms
from django.forms import ModelForm
from TreeFinder.models import FilterRequestObject, UserProfile
from django import forms
from django.contrib.auth.models import User

SPECIES_CHOICES = (
    ("COMMON HORSECHESTNUT", "COMMON HORSECHESTNUT"),
    ("BOWHALL RED MAPLE", "BOWHALL RED MAPLE"),
    ("WHITE ASH", "WHITE ASH"),
    ("KOBUS MAGNOLIA ", "KOBUS MAGNOLIA "),
    ("SHIROFUGEN CHERRY", "SHIROFUGEN CHERRY"),
    ("HEDGE MAPLE", "HEDGE MAPLE"),
    ("JAPANESE HORNBEAM", "JAPANESE HORNBEAM"),
    ("GIANT DOGWOOD", "GIANT DOGWOOD"),
    ("SYCAMORE MAPLE", "SYCAMORE MAPLE"),
    ("TREE LILAC", "TREE LILAC"),
    ("KATSURA TREE", "KATSURA TREE"),
    ("BALSAM FIR ", "BALSAM FIR "),
    ("DOUGLAS FIR", "DOUGLAS FIR"),
    ("AMERICAN MOUNTAIN ASH", "AMERICAN MOUNTAIN ASH"),
    ("GLOBEHEAD NORWAY MAPLE", "GLOBEHEAD NORWAY MAPLE"),
    ("PAPERBARK MAPLE", "PAPERBARK MAPLE"),
    ("PRINCETON GOLD MAPLE", "PRINCETON GOLD MAPLE"),
    ("KWANZAN FLOWERING CHERRY", "KWANZAN FLOWERING CHERRY"),
    ("PISSARD PLUM", "PISSARD PLUM"),
    ("WESTERN RED CEDAR", "WESTERN RED CEDAR"),
    ("SEIBOLDI CHERRY", "SEIBOLDI CHERRY"),
    ("NORWAY MAPLE", "NORWAY MAPLE"),
    ("COLUMNAR NORWAY MAPLE", "COLUMNAR NORWAY MAPLE"),
    ("CRIMEAN LINDEN", "CRIMEAN LINDEN"),
    ("PINK PERFECTION CHERRY", "PINK PERFECTION CHERRY"),
    ("JAPANESE FLOWERING CRABAPPLE", "JAPANESE FLOWERING CRABAPPLE"),
    ("APPRICOT PLUM", "APPRICOT PLUM"),
    ("PYRAMIDAL EUROPEAN BIRCH", "PYRAMIDAL EUROPEAN BIRCH"),
    ("FLOWERING ASH", "FLOWERING ASH"),
    ("RED OAK", "RED OAK"),
    ("AUSTRIAN PINE", "AUSTRIAN PINE"),
    ("DOUGLAS HAWTHORN", "DOUGLAS HAWTHORN"),
    ("JAPANESE MAPLE", "JAPANESE MAPLE"),
    ("EUROPEAN WHITE BIRCH", "EUROPEAN WHITE BIRCH"),
    ("MAZZARD CHERRY", "MAZZARD CHERRY"),
    ("CHANTICLEER PEAR", "CHANTICLEER PEAR"),
    ("ENGLISH HAWTHORN", "ENGLISH HAWTHORN"),
    ("MODESTO ASH", "MODESTO ASH"),
    ("WEEPING CUTLEAF BIRCH", "WEEPING CUTLEAF BIRCH"),
    ("AUTUMN APPLAUSE ASH", "AUTUMN APPLAUSE ASH"),
    ("WATSON'S CRABAPPLE", "WATSON'S CRABAPPLE"),
    ("RAYWOOD ASH", "RAYWOOD ASH"),
    ("PATMORE ASH", "PATMORE ASH"),
    ("WESTERN HEMLOCK", "WESTERN HEMLOCK"),
    ("MOUNTAIN BLACK HEMLOCK", "MOUNTAIN BLACK HEMLOCK"),
    ("LAWSON CYPRESS/PORT ORFORD CED", "LAWSON CYPRESS/PORT ORFORD CED"),
    ("WHITE HIMALAYAN BIRCH", "WHITE HIMALAYAN BIRCH"),
    ("APPLE SPECIES", "APPLE SPECIES"),
    ("TCHONOSKI CRABAPPLE", "TCHONOSKI CRABAPPLE"),
    ("JAPANESE FLOWERING CHERRY ", "JAPANESE FLOWERING CHERRY "),
    ("EUROPEAN ASH", "EUROPEAN ASH"),
    ("PURPLE ROBE LOCUST", "PURPLE ROBE LOCUST"),
    ("WESTOFF'S GLORIE EUROPEAN ASH", "WESTOFF'S GLORIE EUROPEAN ASH"),
    ("NIGHT PURPLE LEAF PLUM", "NIGHT PURPLE LEAF PLUM"),
    ("TUPELO", "TUPELO"),
    ("PYRAMIDAL EUROPEAN HORNBEAM", "PYRAMIDAL EUROPEAN HORNBEAM"),
    ("SILVER VARIEGATED NORWAY MAPLE", "SILVER VARIEGATED NORWAY MAPLE"),
    ("PACIFIC DOGWOOD", "PACIFIC DOGWOOD"),
    ("DAWN REDWOOD", "DAWN REDWOOD"),
    ("EDDIES WHITE WONDER DOGWOOD ", "EDDIES WHITE WONDER DOGWOOD "),
    ("CHERRY, PLUM OR PEACH SPECIES", "CHERRY, PLUM OR PEACH SPECIES"),
    ("PAPER BIRCH", "PAPER BIRCH"),
    ("WATERER GOLDENCHAIN TREE ", "WATERER GOLDENCHAIN TREE "),
    ("UKON JAPANESE CHERRY", "UKON JAPANESE CHERRY"),
    ("SOVEREIGN PIN OAK", "SOVEREIGN PIN OAK"),
    ("LITTLE-LEAF LINDEN", "LITTLE-LEAF LINDEN"),
    ("BOXELDER", "BOXELDER"),
    ("CHINA GIRL DOGWOOD", "CHINA GIRL DOGWOOD"),
    ("DOGWOOD SPECIES", "DOGWOOD SPECIES"),
    ("MIKURUMA-GAESHI CHERRY", "MIKURUMA-GAESHI CHERRY"),
    ("LAVALLEI HYBRID HAWTHORN", "LAVALLEI HYBRID HAWTHORN"),
    ("COMMON APPLE", "COMMON APPLE"),
    ("TAIJA JAPANESE MAPLE", "TAIJA JAPANESE MAPLE"),
    ("PURPLE LEAF SYCAMORE MAPLE", "PURPLE LEAF SYCAMORE MAPLE"),
    ("AMERICAN FILBERT", "AMERICAN FILBERT"),
    ("WORPLESDON SWEETGUM", "WORPLESDON SWEETGUM"),
    ("BRANDON ELM", "BRANDON ELM"),
    ("CRIMSON KING NORWAY MAPLE", "CRIMSON KING NORWAY MAPLE"),
    ("PIN OAK", "PIN OAK"),
    ("BLOODGOOD PLANE TREE", "BLOODGOOD PLANE TREE"),
    ("LONDON PLANE TREE", "LONDON PLANE TREE"),
    ("ARMSTRONG RED MAPLE", "ARMSTRONG RED MAPLE"),
    ("SILVER MAPLE", "SILVER MAPLE"),
    ("SARGENT FLOWERING CHERRY", "SARGENT FLOWERING CHERRY"),
    ("PURPLE PLUM", "PURPLE PLUM"),
    ("RED SUNSET RED MAPLE", "RED SUNSET RED MAPLE"),
    ("AMERICAN ELM", "AMERICAN ELM"),
    ("CAUCASIAN MAPLE", "CAUCASIAN MAPLE"),
    ("BIGLEAF MAPLE", "BIGLEAF MAPLE"),
    ("ATLAS CEDAR", "ATLAS CEDAR"),
    ("ENGLISH HOLLY", "ENGLISH HOLLY"),
    ("BLACK WALNUT", "BLACK WALNUT"),
    ("VILLAGE GREEN ZELKOVA ", "VILLAGE GREEN ZELKOVA "),
    ("DUTCH ELM", "DUTCH ELM"),
    ("RIVER BIRCH", "RIVER BIRCH"),
    ("EUROPEAN MOUNTAIN ASH", "EUROPEAN MOUNTAIN ASH"),
    ("RED MAPLE", "RED MAPLE"),
    ("AKEBONO FLOWERING CHERRY", "AKEBONO FLOWERING CHERRY"),
    ("ENGLISH OAK", "ENGLISH OAK"),
    ("YOSHINO CHERRY", "YOSHINO CHERRY"),
    ("EASTERN REDCEDAR", "EASTERN REDCEDAR"),
    ("JAPANESE SNOWBELL", "JAPANESE SNOWBELL"),
    ("THORNLESS HONEYLOCUST", "THORNLESS HONEYLOCUST"),
    ("SERVICEBERRY", "SERVICEBERRY"),
    ("GRAND FIR", "GRAND FIR"),
    ("CARDINAL ROYAL MOUNTAIN ASH", "CARDINAL ROYAL MOUNTAIN ASH"),
    ("JOSEPH ROCK MOUNTAIN ASH", "JOSEPH ROCK MOUNTAIN ASH"),
    ("WEEPING WILLOW", "WEEPING WILLOW"),
    ("AUTUMN FLAME RED MAPLE", "AUTUMN FLAME RED MAPLE"),
    ("QUEEN ELIZABETH MAPLE", "QUEEN ELIZABETH MAPLE"),
    ("EUROPEAN BEECH", "EUROPEAN BEECH"),
    ("SUGAR MAPLE", "SUGAR MAPLE"),
    ("GINKGO OR MAIDENHAIR TREE", "GINKGO OR MAIDENHAIR TREE"),
    ("CAUCASIAN ASH", "CAUCASIAN ASH"),
    ("HALKA HONEYLOCUST", "HALKA HONEYLOCUST"),
    ("REDBUD CRABAPPLE", "REDBUD CRABAPPLE"),
    ("JAPANESE DOGWOOD", "JAPANESE DOGWOOD"),
    ("NOOTKA CYPRESS", "NOOTKA CYPRESS"),
    ("GIANT SEQUOIA", "GIANT SEQUOIA"),
    ("SHIROTAE(MT FUJI) CHERRY", "SHIROTAE(MT FUJI) CHERRY"),
    ("ARNOLD TULIPTREE", "ARNOLD TULIPTREE"),
    ("PURPLE HAZE JAPANESE PLUM", "PURPLE HAZE JAPANESE PLUM"),
    ("PERSIAN IRONWOOD", "PERSIAN IRONWOOD"),
    ("TOBA HAWTHORN", "TOBA HAWTHORN"),
    ("YELLOW BUCKEYE", "YELLOW BUCKEYE"),
    ("WEEPING CRABAPPLE ", "WEEPING CRABAPPLE "),
    ("SHUBERT RED CHERRY", "SHUBERT RED CHERRY"),
    ("SCOTCH PINE", "SCOTCH PINE"),
    ("GOLDEN GIANT ARBORVITAE", "GOLDEN GIANT ARBORVITAE"),
    ("COMMON LILAC", "COMMON LILAC"),
    ("SHORE PINE", "SHORE PINE"),
    ("PRAIRIE FIRE CRABAPPLE", "PRAIRIE FIRE CRABAPPLE"),
    ("SILVER QUEEN MAPLE", "SILVER QUEEN MAPLE"),
    ("JACK PINE", "JACK PINE"),
    ("CUTLEAF SILVER MAPLE", "CUTLEAF SILVER MAPLE"),
    ("RED JAPANESE MAPLE", "RED JAPANESE MAPLE"),
    ("MAPLE SPECIES", "MAPLE SPECIES"),
    ("COPPER OR PURPLE BEECH", "COPPER OR PURPLE BEECH"),
    ("TRICOLOR DOGWOOD", "TRICOLOR DOGWOOD"),
    ("WEEPING BEECH", "WEEPING BEECH"),
    ("OSAKAZUKI JAPANESE MAPLE", "OSAKAZUKI JAPANESE MAPLE"),
    ("SAWTOOTH OAK", "SAWTOOTH OAK"),
    ("MIYAKO CHERRY ", "MIYAKO CHERRY "),
    ("DEBORAH NORWAY MAPLE", "DEBORAH NORWAY MAPLE"),
    ("TULIPTREE", "TULIPTREE"),
    ("BLACK COTTONWOOD", "BLACK COTTONWOOD"),
    ("SUNBURST HONEYLOCUST", "SUNBURST HONEYLOCUST"),
    ("BUTTERNUT", "BUTTERNUT"),
    ("EMERALD QUEEN NORWAY MAPLE", "EMERALD QUEEN NORWAY MAPLE"),
    ("CALLERY PEAR", "CALLERY PEAR"),
    ("PINK KOUSA DOGWOOD ", "PINK KOUSA DOGWOOD "),
    ("DEODAR CEDAR", "DEODAR CEDAR"),
    ("NORTHWOOD RED MAPLE", "NORTHWOOD RED MAPLE"),
    ("SHADEMASTER HONEYLOCUST", "SHADEMASTER HONEYLOCUST"),
    ("ASH SPECIES", "ASH SPECIES"),
    ("PACIFIC SUNSET MAPLE", "PACIFIC SUNSET MAPLE"),
    ("RUBY RED HORSECHESTNUT", "RUBY RED HORSECHESTNUT"),
    ("FREEMAN'S S.S. MAPLE", "FREEMAN'S S.S. MAPLE"),
    ("BLACK LOCUST", "BLACK LOCUST"),
    ("GOLD LEAF BLACK LOCUST", "GOLD LEAF BLACK LOCUST"),
    ("SPRUCE SPECIES", "SPRUCE SPECIES"),
    ("GOLDEN ORIENTAL ARBORVITAE", "GOLDEN ORIENTAL ARBORVITAE"),
    ("COLUMNAR SARGENT CHERRY", "COLUMNAR SARGENT CHERRY"),
    ("HOLLY SPECIES", "HOLLY SPECIES"),
    ("VARIEGATED SYCAMORE MAPLE", "VARIEGATED SYCAMORE MAPLE"),
    ("WEEPING LAWSON CYPRESS", "WEEPING LAWSON CYPRESS"),
    ("UPRIGHT MOUNTAIN ASH", "UPRIGHT MOUNTAIN ASH"),
    ("RED CAUCASIAN MAPLE", "RED CAUCASIAN MAPLE"),
    ("GOLDEN WHITEBEAM", "GOLDEN WHITEBEAM"),
    ("BLUE ASH", "BLUE ASH"),
    ("CEDAR SPECIES", "CEDAR SPECIES"),
    ("WESTERN CATALPA", "WESTERN CATALPA"),
    ("PINE SPECIES", "PINE SPECIES"),
    ("SUSAN MAGNOLIA", "SUSAN MAGNOLIA"),
    ("PAUL'S SCARLET HAWTHORN", "PAUL'S SCARLET HAWTHORN"),
    ("FULLMOON MAPLE", "FULLMOON MAPLE"),
    ("KOREAN MOUNTAIN ASH", "KOREAN MOUNTAIN ASH"),
    ("GLOBE OR MOPHEAD ACACIA", "GLOBE OR MOPHEAD ACACIA"),
    ("SOUTHERN BEECH", "SOUTHERN BEECH"),
    ("GOLDEN DAWYCK BEECH", "GOLDEN DAWYCK BEECH"),
    ("SKYMASTER ENGLISH OAK", "SKYMASTER ENGLISH OAK"),
    ("ARISTOCRAT PEAR", "ARISTOCRAT PEAR"),
    ("GREEN VASE ZELKOVA", "GREEN VASE ZELKOVA"),
    ("THORNLESS COCKSPUR HAWTHORN", "THORNLESS COCKSPUR HAWTHORN"),
    ("ACCOLADE CHERRY", "ACCOLADE CHERRY"),
    ("DEGROOT LINDEN", "DEGROOT LINDEN"),
    ("COMMON CATALPA", "COMMON CATALPA"),
    ("PANACEK MAPLE", "PANACEK MAPLE"),
    ("WHITE BEAM MOUNTAIN ASH", "WHITE BEAM MOUNTAIN ASH"),
    ("PENDULOUS HYBRID CRABAPPLE", "PENDULOUS HYBRID CRABAPPLE"),
    ("JAPANESE ZELKOVA", "JAPANESE ZELKOVA"),
    ("OCTOBER GLORY RED MAPLE", "OCTOBER GLORY RED MAPLE"),
    ("GREEN COLUMN BLACK MAPLE", "GREEN COLUMN BLACK MAPLE"),
    ("THUNDERCLOUD PURPLE PLUM", "THUNDERCLOUD PURPLE PLUM"),
    ("BERGESON ASH", "BERGESON ASH"),
    ("AUTUMN SPLENDOR CHESTNUT", "AUTUMN SPLENDOR CHESTNUT"),
    ("AMERICAN SWEETGUM", "AMERICAN SWEETGUM"),
    ("SOUTHERN MAGNOLIA", "SOUTHERN MAGNOLIA"),
    ("FRANZ FONTAINE HORNBEAM", "FRANZ FONTAINE HORNBEAM"),
    ("PURPLE FOUNTAIN BEECH", "PURPLE FOUNTAIN BEECH"),
    ("EUROPEAN HORNBEAM", "EUROPEAN HORNBEAM"),
    ("WASHINGTON HAWTHORN", "WASHINGTON HAWTHORN"),
    ("FERNLEAF COPPER BEECH", "FERNLEAF COPPER BEECH"),
    ("SCHWEDLER NORWAY MAPLE", "SCHWEDLER NORWAY MAPLE"),
    ("LEPRECHAUN ASH", "LEPRECHAUN ASH"),
    ("BUR OAK", "BUR OAK"),
    ("DAWYCK'S BEECH", "DAWYCK'S BEECH"),
    ("DOVE OR HANDKERCHIEF TREE", "DOVE OR HANDKERCHIEF TREE"),
    ("VINE MAPLE", "VINE MAPLE"),
    ("AUTUMN BLAZE RED MAPLE", "AUTUMN BLAZE RED MAPLE"),
    ("ALDERLEAFED MOUNTAIN ASH", "ALDERLEAFED MOUNTAIN ASH"),
    ("HARLEQUIN AH", "HARLEQUIN AH"),
    ("GREEN ASH", "GREEN ASH"),
    ("CHINESE WINGNUT", "CHINESE WINGNUT"),
    ("WEEPING KATSURA TREE", "WEEPING KATSURA TREE"),
    ("AUTUMN PURPLE ASH", "AUTUMN PURPLE ASH"),
    ("RED JEWEL CRABAPPLE", "RED JEWEL CRABAPPLE"),
    ("FLOWERING DOGWOOD", "FLOWERING DOGWOOD"),
    ("CAPITAL PEAR", "CAPITAL PEAR"),
    ("LILAC SPECIES", "LILAC SPECIES"),
    ("MEDLAR APPLE", "MEDLAR APPLE"),
    ("ROYALTY CRABAPPLE", "ROYALTY CRABAPPLE"),
    ("SAWARA FALSECYPRESS", "SAWARA FALSECYPRESS"),
    ("FALL GOLD BLACK ASH", "FALL GOLD BLACK ASH"),
    ("VANESSA PERSIAN IRONWOOD", "VANESSA PERSIAN IRONWOOD"),
    ("WHITE SPRUCE", "WHITE SPRUCE"),
    ("SCARLET OAK", "SCARLET OAK"),
    ("CALIFORNIA INCENSE CEDAR", "CALIFORNIA INCENSE CEDAR"),
    ("MORAINE HONEYLOCUST", "MORAINE HONEYLOCUST"),
    ("ELWOOD NORWAY MAPLE", "ELWOOD NORWAY MAPLE"),
    ("GREEN PILLAR PIN OAK", "GREEN PILLAR PIN OAK"),
    ("GOLDEN CAUCASIAN MAPLE", "GOLDEN CAUCASIAN MAPLE"),
    ("AMUR MAPLE", "AMUR MAPLE"),
    ("ROYAL SPLENDOR CRABAPPLE", "ROYAL SPLENDOR CRABAPPLE"),
    ("SNOWCLOUD CRABAPPLE", "SNOWCLOUD CRABAPPLE"),
    ("SUPERFORM NORWAY MAPLE", "SUPERFORM NORWAY MAPLE"),
    ("AMERICAN HORNBEAM", "AMERICAN HORNBEAM"),
    ("RED SHINE FIELD MAPLE ", "RED SHINE FIELD MAPLE "),
    ("CHINESE KOUSA DOGWOOD", "CHINESE KOUSA DOGWOOD"),
    ("WILLOW OAK", "WILLOW OAK"),
    ("SHANTUNG MAPLE ", "SHANTUNG MAPLE "),
    ("RANCHO SARGENT CHERRY", "RANCHO SARGENT CHERRY"),
    ("SNOWBIRD HAWTHORN ", "SNOWBIRD HAWTHORN "),
    ("RUDOLPH CRABAPPLE ", "RUDOLPH CRABAPPLE "),
    ("COMMON HACKBERRY", "COMMON HACKBERRY"),
    ("BLOODGOOD JAPANESE MAPLE", "BLOODGOOD JAPANESE MAPLE"),
    ("APPLE SERVICEBERRY", "APPLE SERVICEBERRY"),
    ("MANCHURIAN CHERRY", "MANCHURIAN CHERRY"),
    ("NORWAY SPRUCE", "NORWAY SPRUCE"),
    ("ELEY FLOWERING CRABAPPLE", "ELEY FLOWERING CRABAPPLE"),
    ("HINOKI FALSECYPRESS", "HINOKI FALSECYPRESS"),
    ("PLUME CRYPTOMERIA", "PLUME CRYPTOMERIA"),
    ("EASTERN HEMLOCK", "EASTERN HEMLOCK"),
    ("BASSWOOD", "BASSWOOD"),
    ("SPECKLED ALDER", "SPECKLED ALDER"),
    ("WEEPING JAPANESE CHERRY", "WEEPING JAPANESE CHERRY"),
    ("LOMBARDY POPLAR", "LOMBARDY POPLAR"),
    ("OAK SPECIES", "OAK SPECIES"),
    ("HAWTHORN SPECIES", "HAWTHORN SPECIES"),
    ("CORNEL DOGWOOD", "CORNEL DOGWOOD"),
    ("AMANOGAWA JAPANESE CHERRY", "AMANOGAWA JAPANESE CHERRY"),
    ("TREE OF HEAVEN", "TREE OF HEAVEN"),
    ("GOLDENRAIN TREE", "GOLDENRAIN TREE"),
    ("EUCALYPTUS", "EUCALYPTUS"),
    ("MONKEY PUZZLE TREE", "MONKEY PUZZLE TREE"),
    ("NORTHERN WHITE CEDAR", "NORTHERN WHITE CEDAR"),
    ("WINDMILL PALM", "WINDMILL PALM"),
    ("MANGLETIA", "MANGLETIA"),
    ("SERBIAN SPRUCE", "SERBIAN SPRUCE"),
    ("COMMON PLUM", "COMMON PLUM"),
    ("PONDEROSA PINE", "PONDEROSA PINE"),
    ("SIBERIAN ELM", "SIBERIAN ELM"),
    ("JAPANESE STEWARTIA", "JAPANESE STEWARTIA"),
    ("EMPRESS TREE", "EMPRESS TREE"),
    ("RED ALDER", "RED ALDER"),
    ("PAPERBARK CHERRY", "PAPERBARK CHERRY"),
    ("ENGLISH ELM", "ENGLISH ELM"),
    ("SCOTS ELM ", "SCOTS ELM "),
    ("STAGHORN SUMAC", "STAGHORN SUMAC"),
    ("SWEETGUM SPECIES", "SWEETGUM SPECIES"),
    ("JAPANESE PAGODA TREE", "JAPANESE PAGODA TREE"),
    ("MORGAN RED MAPLE", "MORGAN RED MAPLE"),
    ("PYRAMIDAL ENGLISH OAK", "PYRAMIDAL ENGLISH OAK"),
    ("MAGNOLIA SPECIES", "MAGNOLIA SPECIES"),
    ("CUCUMBER MAGNOLIA ", "CUCUMBER MAGNOLIA "),
    ("REDLEAF BEECH", "REDLEAF BEECH"),
    ("RED BUCKEYE", "RED BUCKEYE"),
    ("ALPINE FIR", "ALPINE FIR"),
    ("GRAY BIRCH", "GRAY BIRCH"),
    ("SITKA SPRUCE", "SITKA SPRUCE"),
    ("SINGLE SEED HAWTHORN", "SINGLE SEED HAWTHORN"),
    ("FALSECYPRESS SPECIES", "FALSECYPRESS SPECIES"),
    ("HONEYLOCUST", "HONEYLOCUST"),
    ("PURPLE DAWYCK BEECH", "PURPLE DAWYCK BEECH"),
    ("ENGLISH WALNUT", "ENGLISH WALNUT"),
    ("GIANT FILBERT", "GIANT FILBERT"),
    ("WHITCOMB CHERRY", "WHITCOMB CHERRY"),
    ("COMMOM CHOKECHERRY", "COMMOM CHOKECHERRY"),
    ("HIMALAYAN WHITE PINE", "HIMALAYAN WHITE PINE"),
    ("WESTERN WHITE PINE", "WESTERN WHITE PINE"),
    ("EASTERN REDBUD", "EASTERN REDBUD"),
    ("COMMOM JUNIPER", "COMMOM JUNIPER"),
    ("YUNNANENSIS CRABAPPLE", "YUNNANENSIS CRABAPPLE"),
    ("ROSE OF SHARON", "ROSE OF SHARON"),
    ("HORNBEAM SPECIES", "HORNBEAM SPECIES"),
    ("SNOWCONE JAPANESE SNOWBELL", "SNOWCONE JAPANESE SNOWBELL"),
    ("FRAGRANT SNOWBELL", "FRAGRANT SNOWBELL"),
    ("WIER CUTLEAF SILVER MAPLE", "WIER CUTLEAF SILVER MAPLE"),
    ("BLACK MAPLE", "BLACK MAPLE"),
    ("WEEPING GOLDENCHAIN", "WEEPING GOLDENCHAIN"),
    ("YOUNG'S WEEPING BIRCH", "YOUNG'S WEEPING BIRCH"),
    ("GOLDSPOT DOGWOOD", "GOLDSPOT DOGWOOD"),
    ("GOLDEN DESERT ASH", "GOLDEN DESERT ASH"),
    ("MOUNTAIN ASH SPECIES", "MOUNTAIN ASH SPECIES"),
    ("GREAT WHITE CHERRY", "GREAT WHITE CHERRY"),
    ("SAUCER MAGNOLIA", "SAUCER MAGNOLIA"),
    ("COLORADO SPRUCE", "COLORADO SPRUCE"),
    ("GREEN MOUNTAIN NORWAY MAPLE", "GREEN MOUNTAIN NORWAY MAPLE"),
    ("SPANISH CHESTNUT", "SPANISH CHESTNUT"),
    ("GLOBE CATALPA", "GLOBE CATALPA"),
    ("ELM SPECIES", "ELM SPECIES"),
    ("FAIRVIEW NORWAY MAPLE", "FAIRVIEW NORWAY MAPLE"),
    ("COLUMNAR RED MAPLE", "COLUMNAR RED MAPLE"),
    ("MUGO PINE", "MUGO PINE"),
    ("BLACK SPRUCE", "BLACK SPRUCE"),
    ("LEYLAND CYPRESS", "LEYLAND CYPRESS"),
    ("BIGLEAF LINDEN", "BIGLEAF LINDEN"),
    ("REDSPIRE PEAR", "REDSPIRE PEAR"),
    ("PACIFIC MADRONE/ARBUTUS", "PACIFIC MADRONE/ARBUTUS"),
    ("SKYROCKET ENGLISH OAK", "SKYROCKET ENGLISH OAK"),
    ("KARPICK RED MAPLE", "KARPICK RED MAPLE"),
    ("HIGAN CHERRY", "HIGAN CHERRY"),
    ("SNOWDRIFT CRABAPPLE", "SNOWDRIFT CRABAPPLE"),
    ("EASTERN HORNBEAM", "EASTERN HORNBEAM"),
    ("PIN CHERRY", "PIN CHERRY"),
    ("ARBORVITAE SPECIES", "ARBORVITAE SPECIES"),
    ("EASTERN MOUNTAIN MAPLE", "EASTERN MOUNTAIN MAPLE"),
    ("FILBERT SPECIES", "FILBERT SPECIES"),
    ("GOLDEN BEECH", "GOLDEN BEECH"),
    ("YELLOWWOOD", "YELLOWWOOD"),
    ("SUMMIT ASH", "SUMMIT ASH"),
    ("SNAKEBARK MAPLE", "SNAKEBARK MAPLE"),
    ("CHINESE MAGNOLIA ", "CHINESE MAGNOLIA "),
    ("WHITE WILLOW", "WHITE WILLOW"),
    ("FERNLEAF BEECH", "FERNLEAF BEECH"),
    ("YULAN MAGNOLIA ", "YULAN MAGNOLIA "),
    ("ALLGOLD EUROPEAN ASH", "ALLGOLD EUROPEAN ASH"),
    ("KASHMIR CEDAR", "KASHMIR CEDAR"),
    ("PYRAMID BLACK LOCUST", "PYRAMID BLACK LOCUST"),
    ("PURPLE NORWAY MAPLE", "PURPLE NORWAY MAPLE"),
    ("BAUMANN'S SEEDLESS HORSECHESTN", "BAUMANN'S SEEDLESS HORSECHESTN"),
    ("GREY DOGWOOD", "GREY DOGWOOD"),
    ("TRICOLOR BEECH", "TRICOLOR BEECH"),
    ("CRIMSON SENTRY NORWAY MAPLE", "CRIMSON SENTRY NORWAY MAPLE"),
    ("NOBLE FIR", "NOBLE FIR"),
    ("ENGLISH YEW", "ENGLISH YEW"),
    ("EUROPEAN BIRDCHERRY", "EUROPEAN BIRDCHERRY"),
    ("FIR SPECIES ", "FIR SPECIES "),
    ("STRIPED-BARK MAPLE", "STRIPED-BARK MAPLE"),
    ("DAVID'S MAPLE", "DAVID'S MAPLE"),
    ("WILD CHERRY ", "WILD CHERRY "),
    ("GOLDEN RAINDROPS CRABAPPLE", "GOLDEN RAINDROPS CRABAPPLE"),
    ("KENTUCKY COFFEETREE", "KENTUCKY COFFEETREE"),
    ("COMMON FIG", "COMMON FIG"),
    ("CHESTNUT OAK", "CHESTNUT OAK"),
    ("BIG LEAF LINDEN", "BIG LEAF LINDEN"),
    ("CUTLEAF ENGLISH WALNUT", "CUTLEAF ENGLISH WALNUT"),
    ("CHESTNUT SPECIES", "CHESTNUT SPECIES"),
    ("EUROPEAN LARCH", "EUROPEAN LARCH"),
    ("MANCHURIAN BIRCH", "MANCHURIAN BIRCH"),
    ("WHITE FIR", "WHITE FIR"),
    ("SARGENT CRABAPPLE", "SARGENT CRABAPPLE"),
    ("JAPANESE BEECH", "JAPANESE BEECH"),
    ("FRASER'S FIR", "FRASER'S FIR"),
    ("COLORADO BLUE SPRUCE", "COLORADO BLUE SPRUCE"),
    ("GOLDEN CHAIN TREE", "GOLDEN CHAIN TREE"),
    ("ALMIRA NORWAY MAPLE", "ALMIRA NORWAY MAPLE"),
    ("JAPANESE CHESTNUT", "JAPANESE CHESTNUT"),
    ("QUEEN ELIZABETH NORWAY MAPLE", "QUEEN ELIZABETH NORWAY MAPLE"),
    ("WALNUT SPECIES", "WALNUT SPECIES"),
    ("UMBRELLA CATALPA", "UMBRELLA CATALPA"),
    ("OHIO BUCKEYE", "OHIO BUCKEYE"),
    ("JUNIPER SPECIES", "JUNIPER SPECIES"),
    ("CHINESE CRABAPPLE", "CHINESE CRABAPPLE"),
    ("ROSE SARGENT CRABAPPLE", "ROSE SARGENT CRABAPPLE"),
    ("LABURNUM SPECIES", "LABURNUM SPECIES"),
    ("LITTLE LEAF LINDEN", "LITTLE LEAF LINDEN"),
    ("ALDER SPECIES", "ALDER SPECIES"),
    ("BURGANDY LACE JAPANESE  MAPLE", "BURGANDY LACE JAPANESE  MAPLE"),
    ("CAMPERDOWN ELM", "CAMPERDOWN ELM"),
    ("ROYAL RED NORWAY MAPLE", "ROYAL RED NORWAY MAPLE"),
    ("AUTUMN HIGAN CHERRY", "AUTUMN HIGAN CHERRY"),
    ("HOOP'S BLUE SPRUCE", "HOOP'S BLUE SPRUCE"),
    ("NORDMAN FIR", "NORDMAN FIR"),
    ("PYRAMIDAL ARBORVITAE", "PYRAMIDAL ARBORVITAE"),
    ("DWARF SCOTCH PINE", "DWARF SCOTCH PINE"),
    ("SILK TREE", "SILK TREE"),
    ("COLUMNAR SCOTCH PINE", "COLUMNAR SCOTCH PINE"),
    ("AUTUMN GOLD GINKGO", "AUTUMN GOLD GINKGO"),
    ("CRIMSON QUEEN JAPANESE MAPLE", "CRIMSON QUEEN JAPANESE MAPLE"),
    ("CORIGO GIANT DOGWOOD", "CORIGO GIANT DOGWOOD"),
    ("WEEPING HIGAN CHERRY", "WEEPING HIGAN CHERRY"),
    ("SCARLET MAPLE FRANK JR ", "SCARLET MAPLE FRANK JR "),
    ("BLUE ATLAS CEDAR", "BLUE ATLAS CEDAR"),
    ("NORWEGIAN SUNSET MAPLE ", "NORWEGIAN SUNSET MAPLE "),
    ("WEEPING MULBERRY", "WEEPING MULBERRY"),
    ("EASTERN WHITE PINE", "EASTERN WHITE PINE"),
    ("AMERICAN BEECH", "AMERICAN BEECH"),
    ("SHOGETSU JAPANESE CHERRY", "SHOGETSU JAPANESE CHERRY"),
    ("PYRAMIDAL BEECH", "PYRAMIDAL BEECH"),
    ("EUROPEAN LINDEN", "EUROPEAN LINDEN"),
    ("WHITE POPLAR", "WHITE POPLAR"),
    ("INDIA PLUM", "INDIA PLUM"),
    ("BLACK CHERRY", "BLACK CHERRY"),
    ("SPINDLE TREE", "SPINDLE TREE"),
    ("PYRAMIDAL AMERICAN HORNBEAM", "PYRAMIDAL AMERICAN HORNBEAM"),
    ("TRUE SHADE HONEYLOCUST", "TRUE SHADE HONEYLOCUST"),
    ("HUGARIAN OAK", "HUGARIAN OAK"),
    ("AUTUMN GOLD ASH", "AUTUMN GOLD ASH"),
    ("KOTO NO IKO JAPANESE MAPLE", "KOTO NO IKO JAPANESE MAPLE"),
    ("BRANDYWINE RED MAPLE", "BRANDYWINE RED MAPLE"),
    ("ROSTHERN CRABAPPLE", "ROSTHERN CRABAPPLE"),
    ("GOLDEN CATALPA", "GOLDEN CATALPA"),
    ("TREMBLING ASPEN", "TREMBLING ASPEN"),
    ("GLOBE HORNBEAM", "GLOBE HORNBEAM"),
    ("SNOW GOOSE CHERRY", "SNOW GOOSE CHERRY"),
    ("LODGEPOLE PINE", "LODGEPOLE PINE"),
    ("SILVER LINDEN", "SILVER LINDEN"),
    ("DOWNY HAWTHORN", "DOWNY HAWTHORN"),
    ("HYBRID CATALPA", "HYBRID CATALPA"),
    ("THREADLEAF JAPANESE MAPLE", "THREADLEAF JAPANESE MAPLE"),
    ("ORIENTAL SPRUCE", "ORIENTAL SPRUCE"),
    ("WILLOW SPECIES", "WILLOW SPECIES"),
    ("CHINESE TULIPTREE", "CHINESE TULIPTREE"),
    ("TATARIAN MAPLE", "TATARIAN MAPLE"),
    ("CHINESE BIRCH", "CHINESE BIRCH"),
    ("CALIFORNIA REDWOOD", "CALIFORNIA REDWOOD"),
    ("DOUGLAS MAPLE ", "DOUGLAS MAPLE "),
    ("PORTUGUESE LAUREL", "PORTUGUESE LAUREL"),
    ("HENRY MAPLE", "HENRY MAPLE"),
    ("CATALPA SPECIES", "CATALPA SPECIES"),
    ("ROUND LEAF BEECH", "ROUND LEAF BEECH"),
    ("SWEETHEART CHERRY", "SWEETHEART CHERRY"),
    ("ITALIAN PLUM ", "ITALIAN PLUM "),
    ("PEAR SPECIES", "PEAR SPECIES"),
    ("JONAGOLD APPLE", "JONAGOLD APPLE"),
    ("VILMORIN MOUNTAIN ASH", "VILMORIN MOUNTAIN ASH"),
    ("CHANCELLOR LINDEN", "CHANCELLOR LINDEN"),
    ("FREMONT POPLAR", "FREMONT POPLAR"),
    ("SEA BUCKTHORN", "SEA BUCKTHORN"),
    ("PARKWAY MAPLE", "PARKWAY MAPLE"),
    ("COCKSPUR HAWTHORN", "COCKSPUR HAWTHORN"),
    ("SHOJO JAPANESE MAPLE", "SHOJO JAPANESE MAPLE"),
    ("ZENI MAGNOLIA", "ZENI MAGNOLIA"),
    ("MESERVE HOLLY", "MESERVE HOLLY"),
    ("ALLEGHENY SERVICEBERRY", "ALLEGHENY SERVICEBERRY"),
    ("SARATOGA GINKGO", "SARATOGA GINKGO"),
    ("PURPLE CATALPA", "PURPLE CATALPA"),
    ("EVELYN HEDGE MAPLE", "EVELYN HEDGE MAPLE"),
    ("BOSC PEAR", "BOSC PEAR"),
    ("SWEETBAY MAGNOLIA MOONGLOW ", "SWEETBAY MAGNOLIA MOONGLOW "),
    ("MIDGET CRABAPPLE", "MIDGET CRABAPPLE"),
    ("PURPLE GIANT FILBERT", "PURPLE GIANT FILBERT"),
    ("CHITALPA", "CHITALPA"),
    ("JAPANESE BLACK PINE", "JAPANESE BLACK PINE"),
    ("CORNELIAN CHERRY", "CORNELIAN CHERRY"),
    ("CHINESE REDBUD AVONDALE", "CHINESE REDBUD AVONDALE"),
    ("STELLAR PINK DOGWOOD", "STELLAR PINK DOGWOOD"),
    ("ORIENTAL ARBORVITAE", "ORIENTAL ARBORVITAE"),
    ("FAASSEN'S BLACK NORWAY MAPLE", "FAASSEN'S BLACK NORWAY MAPLE"),
    ("JAPANESE ANGELICA TREE", "JAPANESE ANGELICA TREE"),
    ("CORKSCREW WILLOW", "CORKSCREW WILLOW"),
    ("POINTED LEAF MAPLE", "POINTED LEAF MAPLE"),
    ("CHINESE JUNIPER", "CHINESE JUNIPER"),
    ("HILLIER SPIRE CHERRY", "HILLIER SPIRE CHERRY"),
    ("DWARF ALBERTA SPRUCE", "DWARF ALBERTA SPRUCE"),
    ("FIG SPECIES SPECIES", "FIG SPECIES SPECIES"),
    ("DIVERSIFOLIA EUROPEAN ASH", "DIVERSIFOLIA EUROPEAN ASH"),
    ("GOLDEN EUROPEAN ASH ", "GOLDEN EUROPEAN ASH "),
    ("POPLAR SPECIES", "POPLAR SPECIES"),
    ("TURKISH HAZELNUT", "TURKISH HAZELNUT"),
    ("JAPANESE WHITE PINE", "JAPANESE WHITE PINE"),
    ("APRICOT", "APRICOT"),
    ("CASCARA", "CASCARA"),
    ("STAR MAGNOLIA", "STAR MAGNOLIA"),
    ("SUNSPIRE GOLDENCHAIN TREE", "SUNSPIRE GOLDENCHAIN TREE"),
    ("PURPLE LIKIANG SPRUCE", "PURPLE LIKIANG SPRUCE"),
    ("DR. PIRONE'S ASH", "DR. PIRONE'S ASH"),
    ("ORIENTAL PLANE TREE", "ORIENTAL PLANE TREE"),
    ("SMOOTHLEAF ELM", "SMOOTHLEAF ELM"),
    ("GREENLACE NORWAY MAPLE", "GREENLACE NORWAY MAPLE"),
    ("GOLD CLOUD ASH", "GOLD CLOUD ASH"),
    ("GOLDEN WEEPING WILLOW", "GOLDEN WEEPING WILLOW"),
    ("MOSS SAWARA FALSECYPRESS", "MOSS SAWARA FALSECYPRESS"),
    ("SUMAC SPECIES", "SUMAC SPECIES"),
    ("SOURWOOD", "SOURWOOD"),
    ("TEA CRABAPPLE", "TEA CRABAPPLE"),
    ("SOUTHERN SUGAR MAPLE", "SOUTHERN SUGAR MAPLE"),
    ("BLUE NOOTKA CYPRESS", "BLUE NOOTKA CYPRESS"),
    ("PURPLE LEAF HAZELNUT ", "PURPLE LEAF HAZELNUT "),
    ("UPRIGHT PERSIAN IRONWOOD", "UPRIGHT PERSIAN IRONWOOD"),
    ("KOREAN MAPLE", "KOREAN MAPLE"),
    ("VEITCH MAGNOLIA", "VEITCH MAGNOLIA"),
    ("UMBRELLA PINE", "UMBRELLA PINE"),
    ("SIBERIAN CRABAPPLE", "SIBERIAN CRABAPPLE"),
    ("HESSE'S EUROPEAN ASH", "HESSE'S EUROPEAN ASH"),
    ("ASCENDING BALD CYPRESS", "ASCENDING BALD CYPRESS"),
    ("WESTERN LARCH", "WESTERN LARCH"),
    ("HARDY RUBBER TREE", "HARDY RUBBER TREE"),
    ("PIONEER ELM", "PIONEER ELM"),
    ("CONQUEST MAPLE ", "CONQUEST MAPLE "),
    ("OREGON ASH", "OREGON ASH"),
    ("PACIFIC WILLOW", "PACIFIC WILLOW"),
    ("EUROPEAN BLACK ALDER", "EUROPEAN BLACK ALDER"),
    ("MAJESTIC WHITEBEAM", "MAJESTIC WHITEBEAM"),
    ("PURPLE-LEAF HYBRID CRABAPPLE", "PURPLE-LEAF HYBRID CRABAPPLE"),
    ("REGAL PRINCE OAK", "REGAL PRINCE OAK"),
    ("ENGLEMANN SPRUCE", "ENGLEMANN SPRUCE"),
    ("GARRY OAK", "GARRY OAK"),
    ("WEEPING NOOTKA CYPRESS", "WEEPING NOOTKA CYPRESS"),
    ("CELEBRATION RED MAPLE", "CELEBRATION RED MAPLE"),
    ("GLORYBOWER", "GLORYBOWER"),
    ("INGES RUBY VASE IRONWOOD", "INGES RUBY VASE IRONWOOD"),
    ("SHUMARD OAK", "SHUMARD OAK"),
    ("GOLDEN ASH", "GOLDEN ASH"),
    ("CHEROKEE SWEETGUM", "CHEROKEE SWEETGUM"),
    ("VANDERWOLFS PINE", "VANDERWOLFS PINE"),
    ("AMUR CORKTREE", "AMUR CORKTREE"),
    ("MULAN MAGNOLIA ", "MULAN MAGNOLIA "),
    ("GREENLACE JAPANESE MAPLE", "GREENLACE JAPANESE MAPLE"),
    ("PYRAMIDAL SINGLESEED HAWTHORN", "PYRAMIDAL SINGLESEED HAWTHORN"),
    ("VARIEGATED BOX ELDER", "VARIEGATED BOX ELDER"),
    ("TURKISH MOUNTAIN ASH", "TURKISH MOUNTAIN ASH"),
    ("WEEPING SEQUOIA", "WEEPING SEQUOIA"),
    ("OBELISK BEECH", "OBELISK BEECH"),
    ("NORTHERN GEM ASH ", "NORTHERN GEM ASH "),
    ("JAPANESE CRYPTOMERIA", "JAPANESE CRYPTOMERIA"),
    ("GRAY POPLAR", "GRAY POPLAR"),
    ("BALD CYPRESS", "BALD CYPRESS"),
    ("AMERICAN BEAUTY CRABAPPLE", "AMERICAN BEAUTY CRABAPPLE"),
    ("JEFFREY PINE", "JEFFREY PINE"),
    ("WILD DRAGON CHINESE TULIPTREE", "WILD DRAGON CHINESE TULIPTREE"),
    ("AMERICAN CHESTNUT", "AMERICAN CHESTNUT"),
    ("EUROPEAN PURPLE BIRCH", "EUROPEAN PURPLE BIRCH"),
    ("PINK FLOWERING JAPANESE SNOWBE", "PINK FLOWERING JAPANESE SNOWBE"),
    ("SASKATOON BERRY", "SASKATOON BERRY"),
    ("CASTOR ARALIA", "CASTOR ARALIA"),
    ("THREAD-LEAF CYPRESS", "THREAD-LEAF CYPRESS"),
    ("STRAWBERRY TREE", "STRAWBERRY TREE"),
    ("MOUNTAIN SILVERBELL", "MOUNTAIN SILVERBELL"),
    ("EVERGREEN OAK", "EVERGREEN OAK"),
    ("VAUGHN HAWTHORN", "VAUGHN HAWTHORN"),
    ("GOLD HINOKI FALSECYPRESS", "GOLD HINOKI FALSECYPRESS"),
    ("SWEET BAY", "SWEET BAY"),
    ("WHITE MULBERRY", "WHITE MULBERRY"),
    ("SKYLINE HONEYLOCUST", "SKYLINE HONEYLOCUST"),
    ("IVY-LEAVED MAPLE", "IVY-LEAVED MAPLE"),
    ("CAUCASIAN WING NUT", "CAUCASIAN WING NUT"),
    ("JAPANESE WALNUT", "JAPANESE WALNUT"),
    ("CUTLEAF NORWAY MAPLE", "CUTLEAF NORWAY MAPLE"),
    ("HUANGSHAN MAGNOLIA ", "HUANGSHAN MAGNOLIA "),
    ("MICHELIA TREE", "MICHELIA TREE"),
    ("EPAULETTE TREE", "EPAULETTE TREE"),
    ("NANNYBERRY", "NANNYBERRY"),
    ("MAGNOLIA BETTY ", "MAGNOLIA BETTY "),
    ("STINKING ASH", "STINKING ASH"),
    ("CHINESE CATALPA", "CHINESE CATALPA"),
    ("ITALIAN ALDER", "ITALIAN ALDER"),
    ("TURNER'S OAK", "TURNER'S OAK"),
    ("RAINBOW DOGWOOD", "RAINBOW DOGWOOD"),
    ("JADE GREEN NORWAY MAPLE", "JADE GREEN NORWAY MAPLE"),
)

HEIGHT_CHOICES = (
    (1, 1),
    (2, 2),
    (3, 3),
    (4, 4),
    (5, 5),
    (6, 6),
    (7, 7),
    (8, 8),
    (9, 9),
    (10, 10),
)

NEIGHBOURHOOD_CHOICES = (
    ('ARBUTUS RIDGE', 'ARBUTUS RIDGE'),
    ('KITSILANO', 'KITSILANO'),
    ('DUNBAR - SOUTHLANDS', 'DUNBAR - SOUTHLANDS'),
    ('FAIRVIEW', 'FAIRVIEW'),
    ('GRANDVIEW - WOODLANDS', 'GRANDVIEW - WOODLANDS'),
    ('HASTINGS - SUNRISE', 'HASTINGS - SUNRISE'),
    ('KENSINGTON-CEDAR COTTAGE', 'KENSINGTON-CEDAR COTTAGE'),
    ('CITY WIDE', 'CITY WIDE'),
    ('KERRISDALE', 'KERRISDALE'),
    ('KILLARNEY', 'KILLARNEY'),
    ('MARPOLE', 'MARPOLE'),
    ('MOUNT PLEASANT', 'MOUNT PLEASANT'),
    ('OAKRIDGE', 'OAKRIDGE'),
    ('RENFREW - COLLINGWOOD', 'RENFREW - COLLINGWOOD'),
    ('RILEY PARK', 'RILEY PARK'),
    ('SHAUGHNESSY', 'SHAUGHNESSY'),
    ('SOUTH CAMBIE', 'SOUTH CAMBIE'),
    ('STRATHCONA', 'STRATHCONA'),
    ('SUNSET', 'SUNSET'),
    ('VICTORIA - FRASERVIEW', 'VICTORIA - FRASERVIEW'),
    ('WEST END', 'WEST END'),
    ('WEST POINT GREY', 'WEST POINT GREY'),
)

### filtering form code
class FilterRequestObjectForm(ModelForm):
    Species = forms.ChoiceField(label="Species", choices=SPECIES_CHOICES)
    Neighbourhood = forms.ChoiceField(label="Neighbourhood to Search", choices=NEIGHBOURHOOD_CHOICES)
    HeightMin = forms.ChoiceField(label="Minimum Height", choices=HEIGHT_CHOICES)

    class Meta:
        model = FilterRequestObject
        fields = ['Neighbourhood', 'HeightMin', 'Species']

class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = User
        fields = ('username', 'email', 'password')


class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ('website',)

class PasswordForm(forms.ModelForm):
    password = forms.CharField(widget = forms.PasswordInput())

    class meta:
        model = User
        fields = ('password')



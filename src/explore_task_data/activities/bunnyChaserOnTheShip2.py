stage_data = {
    "mission": [
        'mystic1',
        'mystic1',
        'pierce1',
        'burst1',
        'burst1',
        'burst1',
        'burst1',
        'burst1',
        'burst1',
    ],
    "challenge2_sss": {
        'start': [
            ['burst1', (493, 380)],
            ['mystic1', (871, 387)],
            ['pierce1', (1081, 471)]
        ],
        'action': [
            {'t': 'click', 'p': (616, 375), 'ec': True, "desc": "1 right"},
            {'t': 'exchange_and_click', 'p': (721, 333), 'ec': True, "desc": "3 upper left"},
            {'t': 'click', 'p': (571, 420), 'ec': True, 'wait-over': True, "desc": "2 lower right"},

            {'t': 'click', 'p': (557, 333), 'ec': True, "desc": "1 upper right"},
            {'t': 'click', 'p': (694, 558), 'ec': True, "desc": "2 lower left"},
            {'t': 'click_and_teleport', 'p': (896, 360), 'ec': True, 'wait-over': True, "desc": "3 right and tp"},

            {'t': 'click', 'p': (565, 267), 'ec': True, "desc": "1 upper right"},
            {'t': 'click', 'p': (550, 504), 'ec': True, "desc": "2 left"},
            {'t': 'choose_and_change', 'p': (568, 189), "desc": "swap 1 3"},
            {'t': ['exchange', 'click_and_teleport'], 'p': (652, 321), 'ec': True, "desc": "1 choose self and tp"},
            {'t': 'click_and_teleport', 'p': (580, 242), 'wait-over': True, "desc": "3 upper right and tp"},

            {'t': 'click_and_teleport', 'p': (721, 277), 'ec': True, "desc": "1 upper left and tp"},
            {'t': 'click_and_teleport', 'p': (790, 405), 'wait-over': True, "desc": "2 choose self and tp"},
            {'t': 'click', 'p': (391, 384), 'ec': True, "desc": "2 left"},
            {'t': 'click_and_teleport', 'p': (667, 275), 'wait-over': True, "desc": "3 choose self and tp"},
            {'t': 'click', 'p': (880, 288), 'ec': True, 'wait-over': True, "desc": "3 right"},

            {'t': 'exchange_twice_and_click', 'p': (829, 420), 'ec': True, "desc": "3 lower right"},
            {'t': 'exchange_and_click', 'p': (622, 418), 'ec': True, "desc": "2 upper left"},
            {'t': 'choose_and_change', 'p': (622, 418), "desc": "swap 1 2"},
            {'t': 'click', 'p': (680, 328), "desc": "1 upper right"},

        ]
    },
    "challenge2_task": {
        'start': [
            ['burst1', (493, 380)],
            ['mystic1', (871, 387)],
            ['pierce1', (1081, 471)]
        ],
        'action': [
            {'t': 'click', 'p': (616, 375), 'ec': True, "desc": "1 right"},
            {'t': 'exchange_and_click', 'p': (721, 333), 'ec': True, "desc": "3 upper left"},
            {'t': 'click', 'p': (571, 420), 'ec': True, 'wait-over': True, "desc": "2 lower right"},

            {'t': 'click', 'p': (557, 333), 'ec': True, "desc": "1 upper right"},
            {'t': 'click', 'p': (694, 558), 'ec': True, "desc": "2 lower left"},
            {'t': 'click_and_teleport', 'p': (896, 360), 'ec': True, 'wait-over': True, "desc": "3 right and tp"},

            {'t': 'click', 'p': (565, 267), 'ec': True, "desc": "1 upper right"},
            {'t': 'click_and_teleport', 'p': (550, 504), 'ec': True, "desc": "2 left and tp"},
            {'t': 'choose_and_change', 'p': (677, 219), "desc": "swap 1 3"},
            {'t': 'click', 'p': (715, 192), 'wait-over': True, "retreat": (1, 1), "desc": "3 upper right"},

            {'t': 'click_and_teleport', 'p': (637, 387), 'wait-over': True, "desc": "1 choose self and tp"},
            {'t': 'click_and_teleport', 'p': (716, 303), 'ec': True, "desc": "1 upper left and tp"},
            {'t': 'click', 'p': (868, 318), 'wait-over': True, 'ec': True, "desc": "2 right"},

            {'t': 'exchange_and_click', 'p': (832, 426), 'ec': True, "desc": "2 lower right"},
            {'t': 'click', 'p': (628, 443), 'wait-over': True, "desc": "1 right"},

            {'t': 'click', 'p': (683, 359), "desc": "1 upper right"},
        ]
    }
}

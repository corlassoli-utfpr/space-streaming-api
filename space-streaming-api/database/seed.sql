USE space_streaming;

-- Empresas

INSERT INTO empresas (nome, descricao)
VALUES
('SpaceX', 'Empresa privada de exploração espacial e lançamentos orbitais.'),
('NASA', 'Agência espacial dos Estados Unidos.'),
('Rocket Lab', 'Empresa aeroespacial especializada em lançamentos e sistemas espaciais.'),
('Blue Origin', 'Empresa aeroespacial voltada ao desenvolvimento de tecnologias para exploração espacial.'),
('Firefly Aerospace', 'Empresa aeroespacial especializada em lançamentos e veículos espaciais.');


-- Lançamentos

INSERT INTO lancamentos
(nome, data, status, foguete, missao, local, descricao, empresa_id)
VALUES

-- SpaceX
(
    'Falcon Heavy | Demo (Test Flight)',
    '2018-02-06 20:45:00',
    'Launch Successful',
    'Falcon Heavy',
    'Demo Flight 1 (Maiden Flight)',
    'Launch Complex 39A',
    'This will be the inaugural flight of the Falcon Heavy. The test payload will be SpaceX CEO Elon Musk''s midnight cherry Tesla Roadster playing Space Oddity. Destination: An elliptical, heliocentric orbit. Apoapsis: Around Mars'' orbital distance.',
    1
),

(
    'Starship | Integrated Flight Test 5',
    '2024-10-13 12:25:00',
    'Launch Successful',
    'Starship V1',
    'Integrated Flight Test 5',
    'Orbital Launch Pad 1',
    'Fifth test flight of the two-stage Starship launch vehicle.',
    1
),

-- NASA
(
    'SLS Block 1 | Artemis I',
    '2022-11-16 06:47:44',
    'Launch Successful',
    'Space Launch System Block 1',
    'Artemis I',
    'Launch Complex 39B',
    'Artemis I (previously Exploration Mission 1) is the first flight on Space Launch System and the second flight of Orion crew spacecraft. Mission is planned to be an uncrewed circumlunar flight.',
    2
),

(
    'Atlas V 541 | Mars 2020 (Perseverance rover & Ingenuity helicopter)',
    '2020-07-30 11:50:00',
    'Launch Successful',
    'Atlas V 541',
    'Mars 2020 (Perseverance rover & Ingenuity helicopter)',
    'Space Launch Complex 41',
    'Atop this ULA Atlas V rocket will be Perseverance, a car-sized rover which will explore an ancient river delta on Mars. Armed with a suite of six scientific instruments, Perseverance will primarily hunt for clues to the planet''s distant past, and hopefully uncover signs of ancient life and habitability. The rover also carries an experiment that''ll convert carbon dioxide into oxygen, a box-sized helicopter named Ingenuity that''ll demonstrate powered flight on Mars, and a system that enables the rover to leave behind samples for later retrieval and return to Earth during NASA and ESA''s ambitious sample return mission later this decade.',
    2
),

-- Rocket Lab
(
    'Electron | It''s Business Time (Rideshare)',
    '2018-11-11 03:50:00',
    'Launch Successful',
    'Electron',
    'It''s Business Time (Rideshare)',
    'Rocket Lab Launch Complex 1A',
    'Electron''s first commercial launch will feature two Lemur-2 cubesats for Spire Global, a single cubesat for GeoOptics, a NABEO drag sail demonstrator for High Performance Space Structure Systems, an IRVINE01 cubesat from the Irvine CubeSat STEM Program, and two Proxima cubesats from Fleet Space Technologies.',
    3
),

(
    'Electron | Return to Sender (Rideshare)',
    '2020-11-20 02:20:01',
    'Launch Successful',
    'Electron',
    'Return to Sender (Rideshare)',
    'Rocket Lab Launch Complex 1A',
    'Return to Sender will loft 30 satellites to a sun-synchronous orbit at 500 km altitude for a range of customers, including TriSept, Unseenlabs, Swarm, Te Pūnaha Ātea - Auckland Space Institute, and global gaming software company Valve. The satellites span a range of operations, from TriSept''s tech demonstration of new tether systems designed to accelerate spacecraft reentry and reduce orbital debris, through to the next generation of maritime surveillance satellites for Unseenlabs, as well as communications satellites for Swarm. The mission will also deploy New Zealand''s first student-built satellite, the APSS-1 satellite for Te Pūnaha Ātea - Auckland Space Institute at The University of Auckland. The DRAGRACER mission will test the effectiveness of new tether technologies designed to accelerate spacecraft reentry and reduce orbital debris at the conclusion of space missions. TriSept has completed the integration of a pair of qualified Millennium Space Systems 6U small satellites, one featuring the tether drag device and one without. The controlled spacecraft should deorbit in approximately 45 days, while the second spacecraft is expected to remain in orbit for seven to nine years. BRO-2 and BRO-3 are the second and third satellites in French company Unseenlabs'' planned constellation of about 20 satellites dedicated to maritime surveillance. Swarm will launch the latest 24 1/4U SpaceBEE satellites to continue building out its planned constellation of 150 satellites to provide affordable satellite communications services to IoT devices in remote regions around the world. The student-built Waka Āmiorangi Aotearoa APSS-1 satellite is designed to monitor electrical activity in Earth''s upper atmosphere to test whether ionospheric disturbances can predict earthquakes. Extra payload on this flight is a 150 mm 3D printed Half-Life Gnome Chompski. Created for Valve Software''s co-founder Gabe Newell by design studio Weta Workshop, it serves as an homage to the innovation and creativity of gamers worldwide, and also aims to test and qualify a novel 3D printing technique that could be employed for future spacecraft components. Gnome will remain attached to the Kick Stage and will burn up on reentry. Besides payloads, this flight will also serve as a test of Electron''s reusability. Rocket Lab will attempt to bring Electron''s first stage back to Earth under a parachute system for a controlled water landing before collection by a recovery vessel.',
    3
),

-- Blue Origin
(
    'New Shepard | NS-10',
    '2019-01-23 15:05:00',
    'Launch Successful',
    'New Shepard',
    'NS-10',
    'West Texas Suborbital Launch Site/ Corn Ranch',
    'New Shepard flight 10 will feature 9 NASA-sponsored payloads via the NASA Flight opportunity program.',
    4
),

(
    'New Shepard | NS-26',
    '2024-08-29 13:07:03',
    'Launch Successful',
    'New Shepard',
    'NS-26',
    'West Texas Suborbital Launch Site/ Corn Ranch',
    'Twenty-sixth flight of New Shepard carrying six passengers.',
    4
),

-- Firefly Aerospace
(
    'Firefly Alpha | FLTA003 (VICTUS NOX)',
    '2023-09-15 02:28:00',
    'Launch Successful',
    'Firefly Alpha',
    'FLTA003 (VICTUS NOX)',
    'Space Launch Complex 2W',
    'Third flight of the Firefly Alpha small sat launcher, carrying a payload for the US Department of Defense.',
    5
),

(
    'Firefly Alpha | Stairway to Seven',
    '2026-03-12 00:50:00',
    'Launch Successful',
    'Firefly Alpha',
    'Stairway to Seven',
    'Space Launch Complex 2W',
    'Firefly Alpha''s Flight 7 is a test flight and return-To-Flight for the launch vehicle after its April 2025 launch failure. It will test and validate key systems ahead of Firefly''s Block II configuration upgrade on Flight 8 that''s designed to enhance reliability and manufacturability across the vehicle. Flight 7 is the last flown in Alpha''s current configuration and will test multiple Block II subsystems, including the in-house avionics and thermal improvements, to gain flight heritage and validate lessons learned ahead of the full configuration upgrade on Flight 8. This launch also delivered a demonstrator payload for Lockheed Martin.',
    5
);

-- Vídeos

INSERT INTO videos
(titulo, youtube_id, url, thumbnail, duracao, lancamento_id)

VALUES

(
    'Falcon Heavy | Demo (Test Flight)',
    'wbSwFU6tY1c',
    'https://www.youtube.com/watch?v=wbSwFU6tY1c',
    'https://img.youtube.com/vi/wbSwFU6tY1c/hqdefault.jpg',
    NULL,
    1
),

(
    'Starship | Integrated Flight Test 5',
    'hI9HQfCAw64',
    'https://www.youtube.com/watch?v=hI9HQfCAw64',
    'https://img.youtube.com/vi/hI9HQfCAw64/hqdefault.jpg',
    NULL,
    2
),

(
    'SLS Block 1 | Artemis I',
    'zctTKdQcmVA',
    'https://www.youtube.com/watch?v=zctTKdQcmVA',
    'https://img.youtube.com/vi/zctTKdQcmVA/hqdefault.jpg',
    NULL,
    3
),

(
    'Atlas V 541 | Mars 2020',
    'keCc0_8QfL8',
    'https://www.youtube.com/watch?v=keCc0_8QfL8',
    'https://img.youtube.com/vi/keCc0_8QfL8/hqdefault.jpg',
    NULL,
    4
),

(
    'Electron | It''s Business Time',
    'QfBCuK6wEYA',
    'https://www.youtube.com/watch?v=QfBCuK6wEYA',
    'https://img.youtube.com/vi/QfBCuK6wEYA/hqdefault.jpg',
    NULL,
    5
),

(
    'Electron | Return to Sender',
    'NK3rUwGMW8g',
    'https://www.youtube.com/watch?v=NK3rUwGMW8g',
    'https://img.youtube.com/vi/NK3rUwGMW8g/hqdefault.jpg',
    NULL,
    6
),

(
    'New Shepard | NS-10',
    'rJ0nFKyVong',
    'https://www.youtube.com/watch?v=rJ0nFKyVong',
    'https://img.youtube.com/vi/rJ0nFKyVong/hqdefault.jpg',
    NULL,
    7
),

(
    'New Shepard | NS-26',
    'zz6tRqQFU-Q',
    'https://www.youtube.com/watch?v=zz6tRqQFU-Q',
    'https://img.youtube.com/vi/zz6tRqQFU-Q/hqdefault.jpg',
    NULL,
    8
),

(
    'Firefly Alpha | FLTA003 (VICTUS NOX)',
    'P30-FXePPKU',
    'https://www.youtube.com/watch?v=P30-FXePPKU',
    'https://img.youtube.com/vi/P30-FXePPKU/hqdefault.jpg',
    NULL,
    9
),

(
    'Firefly Alpha | Stairway to Seven',
    'nyVbmoRXcvc',
    'https://www.youtube.com/watch?v=nyVbmoRXcvc',
    'https://img.youtube.com/vi/nyVbmoRXcvc/hqdefault.jpg',
    NULL,
    10
);
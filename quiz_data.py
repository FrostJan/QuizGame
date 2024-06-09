def get_quiz_data(category):
    # Define your quiz data here
    quiz_data = {
        "Science": [
            {
                "question": "What is the chemical symbol for oxygen?",
                "choices": ["O2", "O", "O3", "OH"],
                "answer": "O"
            },
            {
                "question": "Which gas do plants absorb during photosynthesis?",
                "choices": ["CO2", "O2", "N2", "H2"],
                "answer": "CO2"
            },
            {
                "question": "What is the main function of red blood cells?",
                "choices": ["Transport Oxygen", "Digest Food", "Produce Hormones", "Filter Toxins"],
                "answer": "Transport Oxygen"
            },
            {
                "question": "What is the Earth's primary source of energy?",
                "choices": ["Wind", "Sun", "Water", "Coal"],
                "answer": "Sun"
            },
            {
                "question": "Which planet is known as the 'Red Planet'?",
                "choices": ["Venus", "Mars", "Jupiter", "Saturn"],
                "answer": "Mars"
            },
            {
                "question": "What is the atomic number of carbon?",
                "choices": ["4", "6", "8", "12"],
                "answer": "6"
            },
            {
                "question": "Which element has the chemical symbol 'Fe'?",
                "choices": ["Iron", "Gold", "Silver", "Copper"],
                "answer": "Iron"
            },
            {
                "question": "What is the largest ocean on Earth?",
                "choices": ["Atlantic", "Indian", "Arctic", "Pacific"],
                "answer": "Pacific"
            },
            {
                "question": "What is the speed of light in a vacuum?",
                "choices": ["300,000 km/s", "500,000 km/s", "700,000 km/s", "900,000 km/s"],
                "answer": "300,000 km/s"
            },
            {
                "question": "Which gas makes up the majority of Earth's atmosphere?",
                "choices": ["Oxygen", "Carbon Dioxide", "Nitrogen", "Argon"],
                "answer": "Nitrogen"
            },
            # Add 5 more questions here
        ],
        "History": [
            {
                "question": "Who was the first Emperor of China?",
                "choices": ["Qin Shi Huang", "Sun Yat-sen", "Mao Zedong", "Emperor Wu"],
                "answer": "Qin Shi Huang"
            },
            {
                "question": "What ancient civilization built the city of Machu Picchu?",
                "choices": ["Maya", "Inca", "Aztec", "Egyptian"],
                "answer": "Inca"
            },
            {
                "question": "In which century did the Renaissance begin?",
                "choices": ["14th", "15th", "16th", "17th"],
                "answer": "14th"
            },
            {
                "question": "Who was the first woman to win a Nobel Prize?",
                "choices": ["Marie Curie", "Rosalind Franklin", "Jane Goodall", "Mother Teresa"],
                "answer": "Marie Curie"
            },
            {
                "question": "What event marked the end of the Cold War?",
                "choices": ["Fall of the Berlin Wall", "Cuban Missile Crisis", "Vietnam War", "Space Race"],
                "answer": "Fall of the Berlin Wall"
            },
            {
                "question": "Which war was fought between North and South Korea in the 1950s?",
                "choices": ["World War I", "Vietnam War", "Korean War", "Gulf War"],
                "answer": "Korean War"
            },
            {
                "question": "Who was the author of 'The Prince'?",
                "choices": ["Machiavelli", "Shakespeare", "Homer", "Plato"],
                "answer": "Machiavelli"
            },
            {
                "question": "Which famous explorer completed the first circumnavigation of the Earth?",
                "choices": ["Christopher Columbus", "Ferdinand Magellan", "Marco Polo", "Captain Cook"],
                "answer": "Ferdinand Magellan"
            },
            {
                "question": "What ancient civilization is known for building the Great Wall of China?",
                "choices": ["Roman", "Greek", "Egyptian", "Chinese"],
                "answer": "Chinese"
            },
            {
                "question": "Who was the leader of the Soviet Union during the Cuban Missile Crisis?",
                "choices": ["Joseph Stalin", "Vladimir Putin", "Nikita Khrushchev", "Mikhail Gorbachev"],
                "answer": "Nikita Khrushchev"
            },
            # Add 5 more questions here
        ],
        "English": [
            {
                "question": "What is the meaning of the word 'ubiquitous'?",
                "choices": ["Rare", "Everywhere", "Unique", "Hidden"],
                "answer": "Everywhere"
            },
            {
                "question": "What is a synonym for 'ephemeral'?",
                "choices": ["Brief", "Permanent", "Eternal", "Stable"],
                "answer": "Brief"
            },
            {
                "question": "What literary device is used when a non-human object is given human characteristics?",
                "choices": ["Irony", "Metaphor", "Simile", "Personification"],
                "answer": "Personification"
            },
            {
                "question": "Which literary work begins with the line 'It was the best of times, it was the worst of times'?",
                "choices": ["Pride and Prejudice", "Jane Eyre", "Great Expectations", "A Tale of Two Cities"],
                "answer": "A Tale of Two Cities"
            },
            {
                "question": "What is the plural form of 'child'?",
                "choices": ["Children", "Childs", "Childes", "Childs"],
                "answer": "Children"
            },
            {
                "question": "What is a synonym for 'ubiquitous'?",
                "choices": ["Rare", "Everywhere", "Unique", "Hidden"],
                "answer": "Everywhere"
            },
            {
                "question": "What is the opposite of 'meticulous'?",
                "choices": ["Careful", "Precise", "Sloppy", "Thorough"],
                "answer": "Sloppy"
            },
            {
                "question": "What is the meaning of the phrase 'bite the bullet'?",
                "choices": ["Chew on a bullet", "Face a difficult situation with courage", "Avoid a challenge", "Bite a piece of metal"],
                "answer": "Face a difficult situation with courage"
            },
            {
                "question": "What does the idiom 'break the ice' mean?",
                "choices": ["Melt ice with heat", "Make a situation more relaxed", "Create an obstacle", "Freeze water"],
                "answer": "Make a situation more relaxed"
            },
            {
                "question": "What is a palindrome?",
                "choices": ["Word spelled the same backward and forward", "A type of rhyme", "A form of poetry", "A form of prose"],
                "answer": "Word spelled the same backward and forward"
            },
            # Add 5 more questions here
        ],
        "Filipino": [
            {
                "question": "Ano ang kahulugan ng salitang 'masipag'?",
                "choices": ["Tamad", "Mahirap", "Madalian", "Makakaya"],
                "answer": "Makakaya"
            },
            {
                "question": "Ano ang tawag sa pag-aayos ng mga halaman upang maging malinis at maayos tignan?",
                "choices": ["Landscape", "Garden", "Flower Arrangement", "Topiary"],
                "answer": "Landscaping"
            },
            {
                "question": "Sino ang tinaguriang 'Ama ng Katipunan'?",
                "choices": ["Andres Bonifacio", "Jose Rizal", "Emilio Aguinaldo", "Apolinario Mabini"],
                "answer": "Andres Bonifacio"
            },
            {
                "question": "Ano ang tinatawag na 'Saging na Saba' sa Ingles?",
                "choices": ["Banana", "Plantain", "Apple", "Orange"],
                "answer": "Plantain"
            },
            {
                "question": "Ano ang tawag sa pag-akyat ng bundok?",
                "choices": ["Camping", "Trekking", "Hiking", "Mountain Climbing"],
                "answer": "Mountain Climbing"
            },
            {
                "question": "Ano ang ibig sabihin ng 'bayanihan'?",
                "choices": ["Pagmamahalan", "Pagkakaisa", "Pagtutulungan", "Pagpapasalamat"],
                "answer": "Pagtutulungan"
            },
            {
                "question": "Ano ang tawag sa sabayang pag-awit?",
                "choices": ["Solo", "Duet", "Choir", "Ensemble"],
                "answer": "Choir"
            },
            {
                "question": "Ano ang tawag sa tanyag na handog ng mga Bicolano sa Pasko?",
                "choices": ["Bibingka", "Puto Bumbong", "Lechon", "Kakanin"],
                "answer": "Kakanin"
            },
            {
                "question": "Sino ang nagsulat ng 'Ibong Adarna'?",
                "choices": ["Jose Rizal", "Andres Bonifacio", "Francisco Balagtas", "Ramon Magsaysay"],
                "answer": "Jose Rizal"
            },
            {
                "question": "Ano ang tawag sa tradisyonal na sayaw na makikita sa mga pista sa probinsiya?",
                "choices": ["Salsa", "Cha-cha", "Tinikling", "Bachata"],
                "answer": "Tinikling"
            },
            # Add 5 more questions here
        ],
        # Add more categories here
    }

    return quiz_data[category]

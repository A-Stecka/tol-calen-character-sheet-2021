# Tol Calen electronic character sheet
The Tol Calen system is the exclusive property of BTA Kompas. 
The system's logo used in the application’s startup window and as the application’s icon is the exclusive property of BTA Kompas. System elements and the logo have been used as components of the project for the course Scripting Languages, created exclusively for personal use. 
The character sheet mechanics are based on the system's rules from 2018–2019.
-

Role-playing games (RPGs) are a combination of story-driven computer games, board games, and improvisational theater. The primary tools for players are the character sheet and dice.  
In the **Tol Calen** system, to which this project is related, the character sheet contains the following elements:

- **Character Concept**: the character’s name, origin, class (available classes: Sly, Scholar, Brave), and the name of the player controlling the character.  
- **6 Attributes**, each with a value between 0 and 5. A total of 15 points can be distributed among them.
- **19 Skills**, each with a value between 0 and 5. A total of 20 points can be distributed among them.
- **Equipment**, including values for armor, shield, and weapons.
- **Affinity**: Whether the character is related to a deity and, therefore, capable of using magic. Having Affinity costs one Attribute Point.
- **Values for Health, Energy, and Initiative**:
  - **Health** is calculated based on Endurance – one point of Endurance equals 6 Health points.
  - **Energy** is calculated based on Charisma (for Sly characters), Intellect (for Scholar characters), or Dexterity (for Brave characters). The Attribute value is multiplied by 2 and added to the Willpower value. If the character has Affinity, they receive one additional Energy point.
  - The base **Initiative** value is the sum of Dexterity and Perception.
- **3 Luck Points**, which allow automatic success on a given test.
- **Experience Points**, which enable character development.

During gameplay, players perform the following actions:

- **Attribute + Skill roll**: Rolling three 10-sided dice. Each die result equal to or lower than the sum of the chosen Attribute and Skill values counts as a success (a roll of 1 always succeeds, and 10 always fails). The number of successes (0, 1, 2, or 3) is counted as the roll result.
  - For example, if the character is a medic performing a healing test, they roll for Intellect + Healing. With an Intellect value of 3 and Healing value of 4, the success threshold is 7.
  - The dice roll results are 2, 7, and 9.
  - Therefore, the roll result is 2 successes.
  
- **Roll against Death**: This is a roll for Endurance + Survival.
  
- **Damage roll**: A roll of as many six-sided dice as the character's weapon value. A roll of 1 or 2 counts as one damage, 3 or 4 as zero damage, and 5 or 6 as two damage. The total number of damage points is then summed.
  - For example, if the character is a warrior using a heavy two-handed sword with a weapon value of 6, they roll 6 dice.
  - The dice results are 1, 1, 5, 6, 5, and 4.
  - The character inflicts 9 damage.
  
- **Initiative roll**: Rolling one 10-sided die and adding the result to the base Initiative value.
  - For example, if the character has Dexterity 2 and Perception 3, the base Initiative is 5.
  - The die roll result is 2.
  - The final Initiative value is 7.

- **Receive and heal damage, and expend and restore Energy**: The amount of damage and Energy used is determined by the Game Master. During healing or Energy restoration, a character’s Health or Energy cannot exceed the base value. A character with zero Energy cannot cast spells, and one with zero Health must roll against Death.

- **Burn Luck Points**: Burning a Luck Point allows automatic success on a test regardless of the roll result or even without rolling. However, burned Luck Points cannot be regained.

- **Gain and spend Experience Points**: One Experience Point can be exchanged for one Attribute Point or three Skill Points.

Players can continue using the same characters across multiple campaigns. At the beginning of each new campaign, they have 3 Luck Points and lose any unspent Experience, Attribute, and Skill Points. All values for Attributes, Skills, and Equipment remain the same.

The main branch contains the project documentation. The application implementation can be found in the app branch.
-

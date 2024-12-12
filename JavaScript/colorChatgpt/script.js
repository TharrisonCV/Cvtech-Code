document.addEventListener("DOMContentLoaded", function () {
    const colors = [
        "red", "green", "blue", "yellow", "orange", "purple",
        "cyan", "pink", "brown", "lime", "teal", "indigo"
    ];

    const shuffledColors = shuffleArray([...colors, ...colors]);
    const gameContainer = document.getElementById("game-container");

    let selectedCards = [];
    let matchedPairs = 0;
    let isFlipping = false;

    // Create the game board
    shuffledColors.forEach(color => {
        const card = document.createElement("div");
        card.className = "card";
        card.dataset.color = color;
        card.addEventListener("click", flipCard);
        gameContainer.appendChild(card);
    });

    function flipCard() {
        if (isFlipping || this === selectedCards[0]) {
            return;
        }

        this.style.backgroundColor = this.dataset.color;
        selectedCards.push(this);

        if (selectedCards.length === 2) {
            isFlipping = true;
            setTimeout(checkMatch, 500);
        }
    }

    function checkMatch() {
        const [card1, card2] = selectedCards;

        if (card1.dataset.color === card2.dataset.color) {
            card1.removeEventListener("click", flipCard);
            card2.removeEventListener("click", flipCard);
            matchedPairs++;

            if (matchedPairs === colors.length) {
                alert("Congratulations! You've matched all pairs.");
                document. location. reload();
            }
        } else {
            setTimeout(() => {
                card1.style.backgroundColor = "#000";
                card2.style.backgroundColor = "#000";
                isFlipping = false;
            }, 50);
        }

        selectedCards = [];
        isFlipping = false;
    }

    function shuffleArray(array) {
        for (let i = array.length - 1; i > 0; i--) {
            const j = Math.floor(Math.random() * (i + 1));
            [array[i], array[j]] = [array[j], array[i]];
        }
        return array;
    }
});

class TypingEffect {
    constructor() {
        this.obs = document.querySelector('.obs')
        this.obstxt = "Esse programa serve para organizar qualquer diretório que esteja desorganizado, colocando-os em pastas separadas por formatos de arquivo."
        this.obsArray = this.obstxt.split('')
    }

    rand(min, max) {
        return Math.floor(Math.random() * (max - min) + min)
    }

    async printer() {
        const print = await setInterval(() => {
                if (this.obsArray.length === 1) clearInterval(print)

                this.obs.innerHTML += this.obsArray.shift()
            }, this.rand(30, 100))
    }
    
    listener() {
        setTimeout(() => this.printer(), 1500)
        
    }
}


const typing = new TypingEffect()
typing.listener()
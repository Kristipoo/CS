("#Oppgave 1")

print("*   *  ****   *****   ****  *****  *****   ***   *   *")
print("*  *   *   *    *    *        *      *    *   *  **  *")
print("* *    *   *    *    *        *      *    *   *  * * *")
print("**     ****     *     ***     *      *    *****  *  **")
print("* *    * *      *        *    *      *    *   *  *   *")
print("*  *   *  *     *        *    *      *    *   *  *   *")
print("*   *  *   *  *****  ****     *    *****  *   *  *   *")

("#Oppgave 2")

fornavn = "Kristian"
etternavn = "Øyen"

print(f"{fornavn} {etternavn}")
print(f"{etternavn}, {fornavn}")


("#Oppgave 3a")

kroner = 250
euro = 25.62
dollar = 29.05

beløp_i_euro = 250 / 25.62
beløp_i_dollar = 250 / 29.05

print(beløp_i_euro)
print(beløp_i_dollar)

print(f"{kroner} NOK tilsvarer {beløp_i_euro:.2f} euro og tilsvarer {beløp_i_dollar:.2f} dollar")


("#oppgave 3b")

print(f"{kroner} NOK tilsvarer {beløp_i_euro:.2f}\N{euro sign} og tilsvarer {beløp_i_dollar:.2f}\N{dollar sign}")

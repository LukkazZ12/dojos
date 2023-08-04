package words

import (
	"testing"
)

func TestChuchuChuchuReturnChuchu(t *testing.T) {
    got := GetMostUsedThreeWords("chuchu chuchu")
    if got[0] != "chuchu" {
        t.Errorf("Esperado: chuchu; Recebido: %s", got[0])
    }
}

func TestSplitText(t *testing.T) {
	got := GetMostUsedThreeWords("qualquer coisa retorna")
	if got[0] != "qualquer" && got[1] != "coisa" && got[2] != "retorna" {
        t.Errorf("Esperado: qualquer coisa retorna; Recebido: %s %s %s", got[0], got[1], got[2])
    } 
}


func TestCheckMostUsedWords(t *testing.T) {
	paragraph := "abacaxi caqui banana caqui abacaxi banana caqui caqui damasco"
	got := GetMostUsedThreeWords(paragraph)
	if got[0] != "abacaxi" || got[1] != "banana" || got[2] != "caqui" {
        t.Errorf("Esperado: abacaxi caqui banana; Recebido: %s %s %s", got[0], got[1], got[2])
    }
}
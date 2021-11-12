/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package balanceadopilas;

import java.util.Scanner;
import java.util.Stack;//clase de pilas

/**
 *
 * @author javie
 */
public class BalanceadoPilas {

    public static void main(String[] args) {
        System.out.println("Escriba la expresión a analizar: ");
        Scanner x = new Scanner(System.in);
        String entrada = x.next();
        Stack<Character> p = new <Character>Stack();// pila de nombre 'p' que almacena caracteres(character)
        int i = 0;
        int tamanio = entrada.length();//longitud de la entrada
        while (i < tamanio) {//mientras i (inicializado en la posición 0) sea menor al tamaño de la entrada
            if ((entrada.charAt(i) == '{') || (entrada.charAt(i)=='(')) {
                p.push('{');
            } else {
                if (p.isEmpty())//en cuanto la pila está vacía sale del bucle
                    break;
                else {
                    p.pop();//saca un elemento de la pila
                }
            }
            i++;//aumenta la posición en i
        }
        if (p.isEmpty() & i == tamanio)//la pila está vacía e i haya llegado al final de la expresión
        {
            System.out.println("La expresión está correctamente balanceada");
        } else {
            System.out.println("La expresión NO está balanceada");
        }
    }

}

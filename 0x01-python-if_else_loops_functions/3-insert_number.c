#include "lists.h"
#include <stdlib.h>
#include <stdio.h>
/**
* insert_node - inserts a number into a sorted singly linked list.  
* @head: pointer to the head of the list
* @number: number to insert
* Return: the address of the new node, or NULL if it failed
*/

listint_t *insert_node(listint_t **head, int number)
{
    listint_t *new_node;
    listint_t *current = *head;

    new_node = malloc(sizeof(listint_t));
    if (new_node == NULL)
        return (NULL);

    new_node->n = number;
    new_node->next = NULL;

    if (*head == NULL)
    {
        *head = new_node;
        return (new_node);
    }

    if (number < current->n)
    {
        new_node->next = current;
        *head = new_node;
        return (new_node);
    }

    while (current->next != NULL)
    {
        if (number >= current->n && number <= current->next->n)
        {
            new_node->next = current->next;
            current->next = new_node;
            return (new_node);
        }
        current = current->next;
    }

    current->next = new_node;
    return (new_node);
}

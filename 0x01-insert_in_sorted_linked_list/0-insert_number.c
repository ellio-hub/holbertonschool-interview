#include "lists.h"
#include <stdlib.h>

/**
 * insert_node - function that inserts number into sorted singly linked list
 * @head: first node in list
 * @number: number to be inserted
 *
 * Return: the address of the new node, or NULL if it failed
*/
listint_t *insert_node(listint_t **head, int number)
{
listint_t *tmp, *new;
tmp = *head;
new = malloc(sizeof(listint_t));
if (new == NULL)
return (NULL);
new->n = number;
if (*head == NULL || (*head)->n >= new->n)
{
new->next = *head;
*head = new;
return (new);
}
for (tmp = *head; tmp != NULL; tmp = tmp->next)
if (tmp->next == NULL || tmp->next->n > new->n)
{
new->next = tmp->next;
tmp->next = new;
break;
}
return (new);
}

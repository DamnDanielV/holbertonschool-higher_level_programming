#include <stdlib.h>
#include "lists.h"
/**
 * insert_node - inserts a number into a sorted singly linked list
 * @head: pointer to head of linked list
 * @number: number to be insert
 *
 * Return: adress of new node or NULL
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *new = malloc(sizeof(listint_t)), *temp = *head;

	new->next = NULL;
	new->n = number;
	if (head == NULL || new == NULL)
		return (NULL);
	if (*head == NULL)
	{
		*head = new;
		return (*head);
	}
	while (temp->next)
	{
		if (new->n >= temp->n && new->n <= temp->next->n)
		{
			new->next = temp->next;
			temp->next = new;
			return (new);
		}
		temp = temp->next;
	}
	return (new);
}

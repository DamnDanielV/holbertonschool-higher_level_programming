#include "lists.h"
#include <stdlib.h>
/**
 * l_node - last node
 * @head: head of the list
 *
 * Return: last node
 */
listint_t *l_node(listint_t *head)
{
	void *prev = NULL;
	listint_t *temp = head;

	while (temp)
	{
		temp->prev = prev;
		prev = temp;
		temp = temp->next;
	}
	temp = head;
	while (temp->next)
		temp = temp->next;
	return (temp);
}
/**
 * is_palindrome - checks if a singly linked list is a palindrome
 * @head: head of the list
 *
 * Return: 0 if it is not a palindrome, 1 if it is a palindrome
 */
int is_palindrome(listint_t **head)
{
	listint_t *node_la = l_node(*head), *temp = *head;

	if (*head && head)
	{
		while (temp != NULL && node_la != NULL)
		{
			if (node_la->n != temp->n)
				return (0);
			temp = temp->next;
			node_la = node_la->prev;
		}
	}
	return (1);
}

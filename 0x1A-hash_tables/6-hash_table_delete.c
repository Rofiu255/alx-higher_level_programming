#include "hash_tables.h"

/**
 * hash_table_delete - deletes a hash table.
 * @ht: the hash table.
 */
void hash_table_delete(hash_table_t *ht)
{
	unsigned long int index = 0;
	hash_node_t *node;

	while (index < ht->size)
	{
		while (ht->array[index] != NULL)
		{
			node = ht->array[index]->next;
			free(ht->array[index]->key);
			free(ht->array[index]->value);
			free(ht->array[index]);
			ht->array[index] = node;
		}
		index++;
	}
	free(ht->array);
	free(ht);
}

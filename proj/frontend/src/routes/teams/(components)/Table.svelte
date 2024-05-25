<script lang="ts">
	import * as Table from '$lib/components/ui/table';
	import type { Team } from '../../../types';
	import { createTable, Render, Subscribe, createRender } from 'svelte-headless-table';
	import { addPagination } from 'svelte-headless-table/plugins';
	import { readable } from 'svelte/store';
	import TableActions from './TableActions.svelte';
	import Button from '$lib/components/ui/button/button.svelte';
	import Services from './ServiceIcons.svelte';

	export let teams: Team[] = [];

	const table = createTable(readable(teams), {
		page: addPagination({
			initialPageSize: 20
		})
	});

	const columns = table.createColumns([
		table.column({
			id: 'id',
			accessor: 'id',
			header: 'Team ID'
		}),
		table.column({
			id: 'name',
			accessor: 'name',
			header: 'Team Name'
		}),
		table.column({
			id: 'services',
			accessor: 'services',
			header: 'Services',
			cell: ({ value }) => createRender(Services, { services: value })
		}),
		table.column({
			accessor: (team) => team,
			header: '',
			cell: ({ value: team, row }) => createRender(TableActions, { team, row })
		})
	]);

	const { headerRows, pageRows, tableAttrs, tableBodyAttrs, pluginStates } =
		table.createViewModel(columns);

	const { hasNextPage, hasPreviousPage, pageIndex } = pluginStates.page;
</script>

<div>
	<div class="rounded-md border">
		<Table.Root {...$tableAttrs}>
			<Table.Header>
				{#each $headerRows as headerRow}
					<Subscribe rowAttrs={headerRow.attrs()}>
						<Table.Row>
							{#each headerRow.cells as cell (cell.id)}
								<Subscribe attrs={cell.attrs()} let:attrs props={cell.props()}>
									<Table.Head {...attrs}>
										<Render of={cell.render()} />
									</Table.Head>
								</Subscribe>
							{/each}
						</Table.Row>
					</Subscribe>
				{/each}
			</Table.Header>
			<Table.Body {...$tableBodyAttrs}>
				{#each $pageRows as row (row.id)}
					<Subscribe rowAttrs={row.attrs()} let:rowAttrs>
						<Table.Row {...rowAttrs} id={`table-row-${row.id}`}>
							{#each row.cells as cell (cell.id)}
								<Subscribe attrs={cell.attrs()} let:attrs>
									<Table.Cell {...attrs}>
										<Render of={cell.render()} />
									</Table.Cell>
								</Subscribe>
							{/each}
						</Table.Row>
					</Subscribe>
				{/each}
			</Table.Body>
		</Table.Root>
	</div>
	<div class="flex items-center justify-end space-x-4 py-4">
		<Button
			variant="outline"
			size="sm"
			on:click={() => ($pageIndex = $pageIndex - 1)}
			disabled={!$hasPreviousPage}
		>
			Previous
		</Button>
		<Button
			variant="outline"
			size="sm"
			on:click={() => ($pageIndex = $pageIndex + 1)}
			disabled={!$hasNextPage}
		>
			Next
		</Button>
	</div>
</div>

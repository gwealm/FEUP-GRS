<script lang="ts">
	import Icon from './Icon.svelte';
	import { page } from '$app/stores';
	import * as Breadcrumb from '$lib/components/ui/breadcrumb/';
	import Auth from './Auth.svelte';

	$: path = $page.url.pathname.split('/');
</script>

<header class="flex h-20 items-center justify-between bg-gray-500 p-5">
	<div class="flex items-center gap-5">
		<Icon name="cloud" height="2em" width="2em" />
		<Breadcrumb.Root>
			<Breadcrumb.List>
				{#each path as pathToken, i (`breadcrumb-${i}`)}
					{@const isLastToken = pathToken === path.at(-1)}
					{@const currentPath = path.slice(0, i + 1).join('/')}

					{#if !isLastToken}
						<Breadcrumb.Item>
							<Breadcrumb.Link
								href={currentPath ? currentPath : '/'}
								data-sveltekit-preload-data="tap">{pathToken ? pathToken : '/'}</Breadcrumb.Link
							>
						</Breadcrumb.Item>
						<Breadcrumb.Separator />
					{:else}
						<Breadcrumb.Item>
							<Breadcrumb.Page>{pathToken}</Breadcrumb.Page>
						</Breadcrumb.Item>
					{/if}
				{/each}
			</Breadcrumb.List>
		</Breadcrumb.Root>
	</div>
	<Auth />
</header>

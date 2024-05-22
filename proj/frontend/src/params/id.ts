import type { ParamMatcher } from "@sveltejs/kit";

export const pattern = /^[\w|\d:.-]*$/i;

export const match: ParamMatcher = (param) => pattern.test(param);
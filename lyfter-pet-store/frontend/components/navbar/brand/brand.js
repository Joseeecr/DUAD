import { brandName } from "./brand-name.js";
import { brandIcon } from "../icons/brand-icon.js";

export function brand(name){

  return `
    <a href="/frontend/pages/home/index.html" class="brand-logo">
      ${brandIcon()}
      ${brandName(name)}
    </a>
  `
}


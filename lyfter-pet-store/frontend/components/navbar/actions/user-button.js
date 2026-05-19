import {userIcon} from "../icons/user-icon.js"

export function userButton() {
  return `
  <a href="#" class="user-profile">
    ${userIcon()}
  </a>
  `
}
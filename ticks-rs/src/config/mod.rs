pub mod keybinding;
pub mod window;

use serde::{Serialize, Deserialize};

#[derive(Serialize, Deserialize, Clone, Debug)]
pub struct Config {
    pub keybindings: Vec<keybinding::Keybinding>,
    pub window: window::Window,
}


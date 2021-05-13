use serde::{Serialize, Deserialize};

#[derive(Serialize, Deserialize, Clone, Debug)]
pub enum BindingType {
    Ticks,
    Command,
}

#[derive(Serialize, Deserialize, Clone, Debug)]
pub struct Keybinding {
    pub squence: String,
    pub t: BindingType,
    pub command: Option<String>
}

pub trait Merge<T = Self, R = Self> {
  fn merge(&mut self, patch: T) -> &mut Self;
  fn into_merge(self, patch: T) -> R
  where Self: Sized;
  fn cloned_merge(&self, patch: &T) -> R
  where
    Self: Sized + Clone,
    T: Clone, {
    self.clone().into_merge(patch.clone())
  }
}
pub trait TryMerge<E = anyhow::Error, T = Self, R = Self> {
  fn try_merge(&self, patch: &T) -> Result<R, E>
  where
    Self: Sized + Clone,
    T: Clone;
}
impl<T, Extendable: Extend<T>, IntoIter: IntoIterator<Item = T>> Merge<IntoIter> for Extendable {
  fn merge(&mut self, patch: IntoIter) -> &mut Self {
    self.extend(patch);
    self
  }
  fn into_merge(mut self, patch: IntoIter) -> Self {
    self.extend(patch);
    self
  }
}
impl<T: Clone + Sized, const SIZE: usize> Merge<Self, Vec<T>> for [T; SIZE] {
  fn merge(&mut self, _: Self) -> &mut Self { unimplemented!() }
  fn into_merge(self, patch: Self) -> Vec<T> { self.to_vec().into_merge(patch) }
}
pub mod json {
  use crate::merge::Merge;
  use serde_json::Value::{self, *};
  pub fn to_vec(base: Value, patch: Value) -> Vec<Value> {
    match (base, patch) {
      (Array(l), Array(r)) => l.into_merge(r),
      (Array(mut l), r) => {
        l.push(r);
        l
      }
      (l, Array(r)) => vec![l].into_merge(r),
      (l, r) => vec![l, r],
    }
  }
  pub fn safe(base: &Value, patch: &Value) -> Option<Value> {
    match (base, patch) {
      (Array(l), Array(r)) => Some(l.cloned_merge(r).into()),
      (Object(l), Object(r)) => Some(l.cloned_merge(r).into()),
      _ => None,
    }
  }
  pub fn force(base: Value, patch: Value) -> Value {
    match (base, patch) {
      (Array(l), Array(r)) => l.into_merge(r).into(),
      (Object(l), Object(r)) => l.into_merge(r).into(),
      (_, r) => r,
    }
  }
  pub fn recursive(base: Value, patch: Value) -> Value {
    match (base, patch) {
      (Array(l), Array(r)) => l.into_merge(r).into(),
      (Object(mut l), Object(r)) => {
        for key_r in r.keys().collect::<Vec<_>>() {
          if l.keys().any(|key| key == key_r) {
            l[key_r] = recursive(l[key_r].clone(), r[key_r].clone());
          }
        }
        l.into()
      }
      (_, r) => r,
    }
  }
  pub mod pefer_array {
    use crate::merge::Merge;
    use serde_json::Value::{self, *};
    pub fn safe(base: &Value, patch: &Value) -> Option<Value> {
      match (base, patch) {
        (Array(l), Array(r)) => Some(l.cloned_merge(r).into()),
        (Array(l), r) => {
          let mut l = l.clone();
          l.push(r.clone());
          Some(l.into())
        }
        (l, Array(r)) => Some(vec![l.clone()].into_merge(r.clone()).into()),
        (Object(l), Object(r)) => Some(l.cloned_merge(r).into()),
        _ => None,
      }
    }
    pub fn force(base: Value, patch: Value) -> Value {
      match (base, patch) {
        (Array(l), Array(r)) => l.into_merge(r).into(),
        (Array(mut l), r) => {
          l.push(r);
          l.into()
        }
        (l, Array(r)) => vec![l].into_merge(r).into(),
        (Object(l), Object(r)) => l.into_merge(r).into(),
        (_, r) => r,
      }
    }
    pub fn recursive(base: Value, patch: Value) -> Value {
      match (base, patch) {
        (Array(l), Array(r)) => l.into_merge(r).into(),
        (Array(mut l), r) => {
          l.push(r);
          l.into()
        }
        (l, Array(r)) => vec![l].into_merge(r).into(),
        (Object(mut l), Object(r)) => {
          for key_r in r.keys().collect::<Vec<_>>() {
            if l.keys().any(|key| key == key_r) {
              l[key_r] = recursive(l[key_r].clone(), r[key_r].clone());
            }
          }
          l.into()
        }
        (_, r) => r,
      }
    }
  }
}

import { create } from 'zustand';
import { fetchMBCMarkdown, parseMBCMarkdown } from './mbc';

export type TCard = {
  sourceUrl: string;
  data: TModelBusinessCard;
}

export type TModelBusinessCardBusinessLogic = {
  name: string;
  description: string;
  tags: string[];
  prompts: string[]; // aliaes
}

export type TModelBusinessCardPrompt = {
  name: string;
  prompt: string;
}

export type TModelBusinessCard = {
  name: string;
  models: string[];
  businessLogics: TModelBusinessCardBusinessLogic[];
  prompts: TModelBusinessCardPrompt[]
}

type TCardStore = {
  cards: TCard[];
  addCard: (sourceUrl: string) => Promise<void>;
}

export const useCardStore = create<TCardStore>((set, get) => ({
  cards: [],
  addCard: async (sourceUrl) => {
    // fetch data from sourceUrl
    const markdown = await fetchMBCMarkdown(sourceUrl)
    // parse data into TModelBusinessCard
    const data = parseMBCMarkdown(markdown)
    // update data store
    set(state => ({
      cards: [...get().cards, { sourceUrl, data }],
    }))
  },
}))




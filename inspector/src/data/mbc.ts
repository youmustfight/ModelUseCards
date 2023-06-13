import { TModelBusinessCard } from "./cardStore";

export const exampleMBCSourceUrls = [
  'https://raw.githubusercontent.com/youmustfight/model-business-cards/main/examples/caselaw_summarizer/model_business_card.md',
  'https://raw.githubusercontent.com/youmustfight/model-business-cards/main/examples/story_generator/model_business_card.md',
];

export const fetchMBCMarkdown = async (sourceUrl: string) => {
  const markdown = await fetch(sourceUrl).then(res => res.text())
  console.log('fetchMBCMarkdown:\n\n', markdown)
  return markdown
}

export const parseMBCMarkdown = (markdown: string): TModelBusinessCard => {
  const name = markdown.match(/# Model Business Card for (.*)/)?.[1]?.trim() ?? "";
  const sections = markdown.split('---')
  const models = sections[1].split('\n-').map((str) => str.trim()).slice(1) // split, trim '\n', and cut out header
  // business logics
  const businessLogics = sections[0].split('###').slice(1).map((str) => str.split('\n\n')).map((strArr) => ({
    name: strArr[0].trim(),
    description: strArr.find(str => str.includes('Description: '))?.replace('Description: ', '').trim() ?? '',
    tags: (strArr.find(str => str.includes('Tags: '))?.replace('Tags: ', '').trim() ?? '')?.split(',').map(str => str.trim()),
    prompts: (strArr.find(str => str.includes('Prompts:'))?.replace('Prompts:', '').trim() ?? '')?.split('\n-').map(str => str.replace('-', '').trim()),
  }))
  // prompt
  const prompts = sections[2].split('###').map((str) => ({
    name: str.slice(0, str.indexOf('\n\n')).trim(),
    prompt: str.slice(str.indexOf('\n\n')).trim().slice(3, -3).trim(),
  })).slice(1) // split, trim '\n', and cut out header

  // RETURN
  const data = {
    name,
    models,
    businessLogics,
    prompts,
  };
  console.log('parseMBCMarkdown:\n\n', data)
  return data
}

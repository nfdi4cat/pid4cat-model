package None;

import java.util.List;
import lombok.*;



/* version: 0.3.0.post26.dev0+e73dc8d */


/**
  An ARK (Archival Resource Key).
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class ArkIdentifier extends RelatedIdentifier {

  private String identifier;
  private String resolvingUrl;

}
